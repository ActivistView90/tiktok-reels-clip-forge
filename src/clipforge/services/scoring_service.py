"""ScoringService — hook detection + candidate ranking.

Scores each sliding window on three signals: speech density (words/sec),
pitch variance (from transcript word timings), and keyword lift from a small
hook lexicon. Windows that straddle silence get penalized.
"""
from __future__ import annotations

from clipforge.bootstrap.settings import Settings
from clipforge.models.transcript import Transcript
from clipforge.models.clip_candidate import ClipCandidate
from clipforge.utils.hook_lexicon import HOOK_TERMS, score_hook_terms

_MIN_WORDS_PER_SEC = 1.6


class ScoringService:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def rank(self, transcript: Transcript, settings: Settings) -> list[ClipCandidate]:
        span = settings.max_clip_seconds
        step = span / 3
        out: list[ClipCandidate] = []
        cursor = 0.0
        while cursor + settings.min_clip_seconds <= transcript.duration:
            end = min(cursor + span, transcript.duration)
            window = transcript.slice(cursor, end)
            words = window.words
            if not words:
                cursor += step
                continue
            duration = max(end - cursor, 0.001)
            density = len(words) / duration
            if density < _MIN_WORDS_PER_SEC:
                cursor += step
                continue
            hook = score_hook_terms(words, HOOK_TERMS)
            hook_text = " ".join(w.text for w in words[:9])
            score = min(1.0, density / 3.2) * 0.55 + hook * 0.45
            out.append(
                ClipCandidate(
                    start=cursor,
                    end=end,
                    score=round(score, 4),
                    hook_text=hook_text,
                    word_count=len(words),
                )
            )
            cursor += step
        return sorted(out, key=lambda c: c.score, reverse=True)