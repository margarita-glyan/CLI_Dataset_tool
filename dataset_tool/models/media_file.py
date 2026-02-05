from dataclasses import dataclass
from pathlib import Path

from dataset_tool.core.hasher import file_sha256


@dataclass(frozen=True)
class MediaFile:
    path: Path

    @property
    def extension(self) -> str:
        return self.path.suffix.lower()

    @property
    def size_bytes(self) -> int:
        return self.path.stat().st_size

    @property
    def sha256(self) -> str:
        """
        File fingerprint (used for duplicate detection).
        """
        return file_sha256(self.path)

    def __str__(self) -> str:
        return str(self.path)
