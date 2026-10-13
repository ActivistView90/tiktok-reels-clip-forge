"""WhisperAdapter — wraps faster-whisper if installed, else fails loud."""
from __future__ import annotations

import logging
from pathlib import Path

from clipforge.models.transcript import Transcript, Word

log = logging.getLogger("clipforge.adapters.whisper")


class WhisperAdapter:
    def __init__(self, model_dir: Path, model_size: str = "small.en") -> None:
        self._model_dir = model_dir
        self._model_size = model_size
        self._model = None

    def _load(self):
        if self._model is not None:
            return self._model
        try:
            from faster_whisper import WhisperModel  # type: ignore
        except ImportError as exc:
            raise RuntimeError(
                "faster-whisper is required for transcription. pip install faster-whisper"
            ) from exc
        self._model_dir.mkdir(parents=True, exist_ok=True)
        self._model = WhisperModel(
            self._model_size,
            device="auto",
            compute_type="int8",
            download_root=str(self._model_dir),
        )
        return self._model

    def transcribe(self, source: Path) -> Transcript:
        model = self._load()
        segments, info = model.transcribe(str(source), word_timestamps=True, vad_filter=True)
        words: list[Word] = []
        for seg in segments:
            for w in seg.words or []:
                words.append(Word(text=w.word.strip(), start=float(w.start), end=float(w.end)))
        return Transcript(words=words, duration=float(info.duration), language=info.language)