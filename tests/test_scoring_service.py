"""ScoringService — window selection, hook weighting, silence rejection."""
from __future__ import annotations

from pathlib import Path

from clipforge.bootstrap.settings import Settings
from clipforge.models.transcript import Transcript, Word
from clipforge.services.scoring_service import ScoringService


def _words(spec: list[tuple[str, float, float]]) -> list[Word]:
    return [Word(text=t, start=s, end=e) for t, s, e in spec]


def test_rank_prefers_hook_dense_windows() -> None:
    words = _words(
        [
            ("nobody", 0.0, 0.3), ("tells", 0.3, 0.6), ("you", 0.6, 0.9),
            ("this", 0.9, 1.2), ("secret", 1.2, 1.6), ("mistake", 1.6, 2.0),
            ("stop", 2.0, 2.3), ("wait", 2.3, 2.6), ("never", 2.6, 3.0),
            ("do", 3.0, 3.2), ("this", 3.2, 3.5), ("again", 3.5, 3.8),
        ]
    )
    # pad to satisfy min_clip_seconds=12 by adding filler at low density on the tail
    for i in range(60):
        t =