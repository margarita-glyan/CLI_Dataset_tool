from dataclasses import dataclass
from dataset_tool.models.media_file import MediaFile


@dataclass(frozen=True)
class TextFile(MediaFile):
    def line_count(self) -> int:
        try:
            return len(self.path.read_text(encoding="utf-8").splitlines())
        except Exception:
            return 0
