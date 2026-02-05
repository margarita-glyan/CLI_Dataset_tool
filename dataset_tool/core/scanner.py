from pathlib import Path

from dataset_tool.models.scan_result import ScanResult


IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}
TEXT_EXTS = {".txt", ".md"}


class Scanner:
    def scan(self, input_dir: Path) -> ScanResult:
        images: list[Path] = []
        texts: list[Path] = []
        unknown: list[Path] = []
        errors: list[str] = []

        input_dir = input_dir.expanduser().resolve()

        if not input_dir.exists():
            return ScanResult([], [], [], [f"Path not found: {input_dir}"])

        if not input_dir.is_dir():
            return ScanResult([], [], [], [f"Not a directory: {input_dir}"])

        for path in input_dir.rglob("*"):
            if path.is_dir():
                continue

            ext = path.suffix.lower()

            if ext in IMAGE_EXTS:
                images.append(path)
            elif ext in TEXT_EXTS:
                texts.append(path)
            else:
                unknown.append(path)

        return ScanResult(images, texts, unknown, errors)
