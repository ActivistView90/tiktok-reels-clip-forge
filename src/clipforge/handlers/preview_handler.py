"""Preview handler — dry-run scoring report as a compact table for stdout."""
from __future__ import annotations

from clipforge.models.clip_candidate import ClipCandidate


def format_preview(candidates: list[ClipCandidate], limit: int = 20) -> str:
    rows = ["  #  score  start    end      hook"]
    for i, c in enumerate(sorted(candidates, key=lambda x: x.score, reverse=True)[:limit], 1):
        rows.append(
            f"{i:>3}  {c.score:5.2f}  {c.start:6.2f}s  {c.end:6.2f}s   {c.hook_text[:42]!r}"
        )
    return "\n".join(rows)