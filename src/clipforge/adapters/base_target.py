"""BaseTargetAdapter — contract every TikTok/Reels/Shorts adapter implements."""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from clipforge.models.clip_candidate import ClipCandidate


@dataclass(slots=True)
class RenderSpec:
    width: int
    height: int
    fps: int
    video_bitrate: str
    audio_bitrate: str
    subtitle_cues: list[tuple[float, float, str]]


class BaseTargetAdapter(ABC):
    name: str = "base"

    @abstractmethod
    def render_spec(self, candidate: ClipCandidate, phrases: list[tuple[float, float, str]]) -> RenderSpec: ...