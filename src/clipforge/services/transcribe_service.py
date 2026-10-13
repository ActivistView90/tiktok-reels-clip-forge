"""TranscribeService — wraps the whisper adapter, caches results on disk.

Cache key is sha1(source path + size + mtime). Cache dir lives next to the
model dir so a fresh checkout shares nothing and a stale checkout invalidates
cleanly. Cache entries are JSON; safe to delete.
"""
from __future__ import annotations

import hashlib
import json
import logging
from pathlib import Path

from clipforge.adapters.whisper_adapter import WhisperAdapter
from clipforge.bootstrap.settings import Settings
from clipforge.models.transcript import Transcript

log = logging.getLogger("clipforge.services.transcribe")


class TranscribeService:
    def __init__(self, whisper: WhisperAdapter, settings: Settings) -> None:
        self._whisper = whisper
        self._cache_dir = settings.model_dir.parent / "transcripts"
        self._cache_dir.mkdir(parents=True, exist_ok=True)

    def _cache_key(self, source: Path) -> str:
        st = source.stat()
        blob = f"{source.resolve()}|{st.st_size}|{int(st.st_mtime)}".encode("utf-8")
        return hashlib.sha1(blob).hexdigest()[:16]

    def transcribe(self, source: Path) -> Transcript:
        key = self._cache_key(source)
        cached = self._cache_dir / f"{key}.json"
        if cached.is_file():
            log.debug("transcript cache hit: %s", key)
            return Transcript.from_dict(json.loads(cached.read_text(encoding="utf-8")))
        transcript = self._whisper.transcribe(source)
        cached.write_text(json.dumps(transcript.to_dict()), encoding="utf-8")
        return transcript