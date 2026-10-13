"""Transcript + Word — immutable-ish, JSON-serializable, sliceable by time."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Word:
    text: str
    start: float
    end: float

    def to_dict(self) -> dict:
        return {"text": self.text, "start": self.start, "end": self.end}


@dataclass(slots=True)
class Transcript:
    words: list[Word] = field(default_factory=list)
    duration: float = 0.0
    language: str = "en"

    def slice(self, start: float, end: float) -> "Transcript":
        picked = [w for w in self.words if w.end >= start and w.start <= end]
        return Transcript(words=picked, duration=end - start, language=self.language)

    def to_dict(self) -> dict:
        return {
            "words": [w.to_dict() for w in self.words],
            "duration": self.duration,
            "language": self.language,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Transcript":
        return cls(
            words=[Word(**w) for w in data.get("words", [])],
            duration=float(data.get("duration", 0.0)),
            language=data.get("language", "en"),
        )