"""CaptionService — plans burned-in caption phrases per candidate clip.

Style presets live in config/caption_styles.toml. Phrases are chunked to
<= 4 words so TikTok's burned captions stay readable on a 9:16 crop.
"""
from __future__ import annotations

from clipforge.bootstrap.settings import Settings
from clipforge.models.transcript import Transcript, Word
from clipforge.models.clip_candidate import ClipCandidate

_MAX_WORDS_PER_CUE = 4


class CaptionService:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def plan_captions(self, transcript: Transcript, candidate: ClipCandidate, settings: Settings) -> list[tuple[float, float, str]]:
        words: list[Word] = transcript.slice(candidate.start, candidate.end).words
        cues: list[tuple[float, float, str]] = []
        buf: list[Word] = []
        for w in words:
            buf.append(w)
            if len(buf) >= _MAX_WORDS_PER_CUE or w.text.endswith((".", "?", "!", ",")):
                cues.append((buf[0].start - candidate.start, buf[-1].end - candidate.start, " ".join(x.text for x in buf)))
                buf = []
        if buf:
            cues.append((buf[0].start - candidate.start, buf[-1].end - candidate.start, " ".join(x.text for x in buf)))
        return cues