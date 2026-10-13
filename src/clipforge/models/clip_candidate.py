"""ClipCandidate — a scored window ready for caption + render."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ClipCandidate:
    start: float
    end: float
    score: float
    hook_text: str
    word_count: int

    @property
    def duration(self) -> float:
        return self.end - self.start

    def to_dict(self) -> dict:
        return {
            "start": self.start,
            "end": self.end,
            "score": self.score,
            "hook_text": self.hook_text,
            "word_count": self.word_count,
        }