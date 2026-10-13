"""PipelineService — the top-level orchestration for one source video."""
from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

from clipforge.bootstrap.settings import Settings
from clipforge.services.caption_service import CaptionService
from clipforge.services.render_service import RenderService
from clipforge.services.scoring_service import ScoringService
from clipforge.services.transcribe_service import TranscribeService

log = logging.getLogger("clipforge.services.pipeline")


@dataclass(slots=True)
class PipelineReport:
    source: Path
    candidates: int
    emitted: int


class PipelineService:
    def __init__(
        self,
        transcribe: TranscribeService,
        scoring: ScoringService,
        caption: CaptionService,
        render: RenderService,
        settings: Settings,
    ) -> None:
        self._transcribe = transcribe
        self._scoring = scoring
        self._caption = caption
        self._render = render
        self._settings = settings

    def run(self, source: Path, out_dir: Path, max_clips: int, target: str, dry_run: bool) -> PipelineReport:
        if not source.exists():
            raise FileNotFoundError(str(source))
        out_dir.mkdir(parents=True, exist_ok=True)

        transcript = self._transcribe.transcribe(source)
        candidates = self._scoring.rank(transcript, self._settings)
        log.info("%s -> %d candidate window(s)", source.name, len(candidates))
        if dry_run:
            return PipelineReport(source=source, candidates=len(candidates), emitted=0)

        emitted = 0
        for cand in candidates[:max_clips]:
            phrases = self._caption.plan_captions(transcript, cand, self._settings)
            self._render.emit(source=source, candidate=cand, phrases=phrases, out_dir=out_dir, target=target)
            emitted += 1
        return PipelineReport(source=source, candidates=len(candidates), emitted=emitted)