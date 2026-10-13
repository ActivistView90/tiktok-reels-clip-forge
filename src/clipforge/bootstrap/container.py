"""Tiny DI container. Services are wired once at startup, no framework."""
from __future__ import annotations

from dataclasses import dataclass

from clipforge.bootstrap.settings import Settings
from clipforge.services.caption_service import CaptionService
from clipforge.services.pipeline_service import PipelineService
from clipforge.services.render_service import RenderService
from clipforge.services.scoring_service import ScoringService
from clipforge.services.transcribe_service import TranscribeService
from clipforge.adapters.ffmpeg_adapter import FFmpegAdapter
from clipforge.adapters.whisper_adapter import WhisperAdapter
from clipforge.adapters.tiktok_adapter import TikTokAdapter
from clipforge.adapters.reels_adapter import ReelsAdapter


@dataclass(slots=True)
class Container:
    pipeline: PipelineService
    settings: Settings


def build_container(settings: Settings) -> Container:
    ffmpeg = FFmpegAdapter(binary=settings.ffmpeg_binary, threads=settings.encode_threads)
    whisper = WhisperAdapter(model_dir=settings.model_dir, model_size=settings.whisper_size)
    target_adapter = TikTokAdapter() if settings.default_target == "tiktok" else ReelsAdapter()

    transcribe = TranscribeService(whisper=whisper, settings=settings)
    scoring = ScoringService(settings=settings)
    caption = CaptionService(settings=settings)
    render = RenderService(ffmpeg=ffmpeg, target=target_adapter, settings=settings)
    pipeline = PipelineService(
        transcribe=transcribe,
        scoring=scoring,
        caption=caption,
        render=render,
        settings=settings,
    )
    return Container(pipeline=pipeline, settings=settings)