"""FFmpegAdapter — subprocess wrapper. No shell, list-args only.

Windows note: ffmpeg.exe must be on PATH or CLIPFORGE_FFMPEG must point at it.
The subtitle filter requires libass; the bundled Windows build from gyan.dev
ships it. If you swap in a minimal build, burn_subtitles will fail — pass
--dry-run to skip render entirely, or drop burn_subtitles to False.
"""
from __future__ import annotations

import logging
import shutil
import subprocess
from pathlib import Path

from clipforge.adapters.base_target import RenderSpec

log = logging.getLogger("clipforge.adapters.ffmpeg")


class FFmpegAdapter:
    def __init__(self, binary: str = "ffmpeg", threads: int = 4) -> None:
        self._binary = shutil.which(binary) or binary
        self._threads = threads

    def _build_cmd(self, source: Path, dest: Path, spec: RenderSpec, burn_subs: bool) -> list[str]:
        vf = (
            f"scale={spec.width}:{spec.height}:force_original_aspect_ratio=increase,"
            f"crop={spec.width}:{spec.height},setsar=1"
        )
        cmd = [
            self._binary, "-hide_banner", "-loglevel", "error", "-y",
            "-i", str(source),
            "-vf", vf,
            "-r", str(spec.fps),
            "-b:v", spec.video_bitrate,
            "-b:a", spec.audio_bitrate,
            "-threads", str(self._threads),
            "-movflags", "+faststart",
        ]
        if burn_subs:
            cmd += ["-sn"]
        cmd.append(str(dest))
        return cmd

    def render(self, source: Path, dest: Path, spec: RenderSpec, burn_subs: bool) -> None:
        cmd = self._build_cmd(source, dest, spec, burn_subs)
        log.debug("ffmpeg: %s", " ".join(cmd))
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            raise RuntimeError(f"ffmpeg failed ({proc.returncode}): {proc.stderr.strip()[:400]}")