"""Minimal FastAPI surface for the desktop UI / local automation.

Run with: `uvicorn clipforge.api.app:app --port 8765`.
Not required for CLI usage — this exists so the desktop shell (src/desktop/)
and third-party automations have a stable contract.
"""
from __future__ import annotations

from pathlib import Path

try:
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
except ImportError:  # pragma: no cover - optional dep
    raise SystemExit("fastapi + pydantic required for the API layer: pip install fastapi uvicorn")

from clipforge.bootstrap.container import build_container
from clipforge.bootstrap.settings import load_settings

app = FastAPI(title="tiktok-reels-clip-forge", version="0.7.3")
_settings = load_settings(Path.cwd() / "config" / "clipforge.toml")
_container = build_container(_settings)


class GenerateRequest(BaseModel):
    source: str
    out_dir: str = "clips"
    count: int = 8
    target: str = "tiktok"
    dry_run: bool = False


@app.post("/generate")
def generate(req: GenerateRequest) -> dict:
    src = Path(req.source)
    if not src.exists():
        raise HTTPException(status_code=404, detail=f"source not found: {src}")
    report = _container.pipeline.run(
        source=src, out_dir=Path(req.out_dir), max_clips=req.count, target=req.target, dry_run=req.dry_run
    )
    return {"emitted": report.emitted, "candidates": report.candidates, "source": str(report.source)}