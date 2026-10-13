"""Stable, sortable filenames for rendered clips."""
from __future__ import annotations

import re

_SLUG_RE = re.compile(r"[^a-z0-9]+")


def clip_slug(source_stem: str, start_seconds: float, score: float) -> str:
    base = _SLUG_RE.sub("_", source_stem.lower()).strip("_") or "clip"
    return f"{base}_{int(start_seconds):05d}s_{score:.2f}".replace(".", "p")