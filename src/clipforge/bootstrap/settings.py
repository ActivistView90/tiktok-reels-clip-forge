"""Settings loader. TOML on disk, defaults in code, env override via CLIPFORGE_*."""
from __future__ import annotations

import os
import tomllib
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class Settings:
    ffmpeg_binary: str = "ffmpeg"
    encode_threads: int = 4
    model_dir: Path = field(default_factory=lambda: Path.home() / ".clipforge" / "models")
    whisper_size: str = "small.en"
    default_target: str = "tiktok"
    min_clip_seconds: float = 12.0
    max_clip_seconds: float = 58.0
    hook_window_seconds: float = 3.5
    caption_style: str = "karaoke_yellow"
    burn_subtitles: bool = True


_ENV_MAP = {
    "CLIPFORGE_FFMPEG": "ffmpeg_binary",
    "CLIPFORGE_THREADS": ("encode_threads", int),
    "CLIPFORGE_MODEL_DIR": ("model_dir", Path),
    "CLIPFORGE_WHISPER": "whisper_size",
    "CLIPFORGE_TARGET": "default_target",
}


def load_settings(path: Path) -> Settings:
    data: dict = {}
    if path.is_file():
        with path.open("rb") as fh:
            data = tomllib.load(fh)
    flat = {**data.get("clipforge", {}), **(data.get("render", {}))}
    kwargs = {k: v for k, v in flat.items() if hasattr(Settings, k) or k in Settings.__dataclass_fields__}
    settings = Settings(**kwargs)
    for env_key, mapping in _ENV_MAP.items():
        raw = os.environ.get(env_key)
        if raw is None:
            continue
        if isinstance(mapping, tuple):
            name, caster = mapping
            setattr(settings, name, caster(raw))
        else:
            setattr(settings, mapping, raw)
    return settings