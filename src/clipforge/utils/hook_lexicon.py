"""Hook lexicon — terms that correlate with scroll-stopping openers.

Curated from ~4k viral short-form transcripts (2024-2025). Weighted by
average retention lift. Keep this list under ~120 entries; past that the
signal flattens.
"""
from __future__ import annotations

from clipforge.models.transcript import Word

HOOK_TERMS: dict[str, float] = {
    "you": 0.4, "never": 1.2, "always": 0.9, "nobody": 1.3, "everyone": 0.8,
    "secret": 1.5, "truth": 1.1, "mistake": 1.4, "stop": 1.2, "wait": 1.0,
    "actually": 0.7, "literally": 0.6, "imagine": 1.1, "here's": 0.9,
    "why": 1.0, "how": 0.7, "what": 0.6, "watch": 1.3, "listen": 0.9,
    "bro": 0.5, "insane": 1.2, "wild": 1.0, "crazy": 1.1, "scam": 1.4,
    "broke": 0.9, "rich": 1.0, "hack": 1.2, "trick": 0.9, "free": 0.8,
}


def score_hook_terms(words: list[Word], lexicon: dict[str, float]) -> float:
    if not words:
        return 0.0
    head = words[:12]
    total = 0.0
    for w in head:
        token = w.text.lower().strip(".,!?;:\"'")
        total += lexicon.get(token, 0.0)
    return min(1.0, total / 4.0)