from dataclasses import dataclass
from pathlib import Path


@dataclass
class ScanResult:
    images: list[Path]
    texts: list[Path]
    unknown: list[Path]
    errors: list[str]

    @property
    def total_files(self) -> int:
        return len(self.images) + len(self.texts) + len(self.unknown)
