"""TikTok adapter — 1080x1920, 30fps, safe-area aware caption bottom margin."""
from __future__ import annotations

from clipforge.adapters.base_target import BaseTargetAdapter, RenderSpec
from clipforge.models.clip_candidate import ClipCandidate

TIKTOK_SAFE_BOTTOM_RATIO = 0.12


class TikTokAdapter(BaseTargetAdapter):
    name = "tiktok"

    def render_spec(self, candidate: ClipCandidate, phrases: list[tuple[float, float, str]]) -> RenderSpec:
        return RenderSpec(
            width=1080,
            height=1920,
            fps=30,
            video_bitrate="8M",
            audio_bitrate="192k",
            subtitle_cues=phrases,
        )