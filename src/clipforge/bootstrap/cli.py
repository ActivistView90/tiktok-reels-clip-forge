"""Thin CLI handler. Parses argv, builds the service container, dispatches."""
from __future__ import annotations

import argparse
import logging
from pathlib import Path

from clipforge.bootstrap.container import build_container
from clipforge.bootstrap.settings import load_settings

log = logging.getLogger("clipforge.cli")


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="clipforge", description="AI short-form clip generator (TikTok/Reels)")
    p.add_argument("source", type=Path, help="Long-form video file or watch folder.")
    p.add_argument("-o", "--out", type=Path, default=Path("clips"), help="Output directory for rendered clips.")
    p.add_argument("-n", "--count", type=int, default=8, help="Max clips to emit per source.")
    p.add_argument("--target", choices=["tiktok", "reels", "shorts"], default="tiktok")
    p.add_argument("--dry-run", action="store_true", help="Score only, skip render + caption.")
    p.add_argument("-v", "--verbose", action="store_true")
    return p


def main(argv: list[str]) -> int:
    args = _build_parser().parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)-7s %(name)s :: %(message)s",
    )
    settings = load_settings(Path.cwd() / "config" / "clipforge.toml")
    container = build_container(settings)
    try:
        report = container.pipeline.run(
            source=args.source,
            out_dir=args.out,
            max_clips=args.count,
            target=args.target,
            dry_run=args.dry_run,
        )
    except FileNotFoundError as exc:
        log.error("source not found: %s", exc)
        return 2
    log.info("emitted %d clip(s) -> %s", report.emitted, args.out)
    return 0