"""Batch handler — walks a watch folder, hands each file to the pipeline."""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Iterable

from clipforge.services.pipeline_service import PipelineService

log = logging.getLogger("clipforge.handlers.batch")
VIDEO_EXTS = {".mp4", ".mkv", ".mov", ".webm", ".m4v"}


def iter_sources(watch: Path) -> Iterable[Path]:
    if watch.is_file():
        yield watch
        return
    for entry in sorted(watch.rglob("*")):
        if entry.suffix.lower() in VIDEO_EXTS:
            yield entry


def run_batch(pipeline: PipelineService, watch: Path, out_dir: Path, max_clips: int) -> int:
    total = 0
    for source in iter_sources(watch):
        log.info("processing source: %s", source.name)
        report = pipeline.run(source=source, out_dir=out_dir / source.stem, max_clips=max_clips, target="tiktok", dry_run=False)
        total += report.emitted
    return total