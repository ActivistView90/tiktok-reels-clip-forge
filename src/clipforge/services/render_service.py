"""RenderService — asks the platform adapter for a crop spec, then renders."""
from __future__ import annotations

import logging
from pathlib import Path

from clipforge.adapters.ffmpeg_adapter import FFmpegAdapter
from clipforge.adapters.base_target import BaseTargetAdapter
from clipforge.bootstrap.settings import Settings
from clipforge.models.clip_candidate import ClipCandidate
from clipforge.utils.filename import clip_slug

log = logging.getLogger("clipforge.services.render")


class RenderService:
    def __init__(self, ffmpeg: FFmpegAdapter, target: BaseTargetAdapter, settings: Settings) -> None:
        self._ffmpeg = ffmpeg
        self._target = target
        self._settings = settings

    def emit(
        self,
        source: Path,
        candidate: ClipCandidate,
        phrases: list[tuple[float, float, str]],
        out_dir: Path,
        target: str,
    ) -> Path:
        slug = clip_slug(source.stem, candidate.start, candidate.score)
        dest = out_dir / f"{slug}.mp4"
        spec = self._target.render_spec(candidate, phrases)
        self._ffmpeg.render(source=source, dest=dest, spec=spec, burn_subs=self._settings.burn_subtitles)
        log.info("rendered %s (score=%.2f)", dest.name, candidate.score)
        return dest