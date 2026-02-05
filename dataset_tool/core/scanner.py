from pathlib import Path
import logging

from dataset_tool.models.image_file import ImageFile
from dataset_tool.models.scan_result import ScanResult
from dataset_tool.models.text_file import TextFile

logger = logging.getLogger(__name__) 

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}
TEXT_EXTS = {".txt", ".md"}


class Scanner:
    def scan(self, input_dir: Path) -> ScanResult:
        images: list[ImageFile] = []
        texts: list[TextFile] = []
        unknown: list[str] = []
        errors: list[str] = []

        input_dir = input_dir.expanduser().resolve()

        logger.info(f"Scanning folder: {input_dir}")

        if not input_dir.exists():
            return ScanResult([], [], [], [f"Path not found: {input_dir}"])

        if not input_dir.is_dir():
            return ScanResult([], [], [], [f"Not a directory: {input_dir}"])

        for path in input_dir.rglob("*"):
            if path.is_dir():
                continue

            ext = path.suffix.lower()

            if ext in IMAGE_EXTS:
                images.append(ImageFile(path))
            elif ext in TEXT_EXTS:
                texts.append(TextFile(path))
            else:
                logger.warning(f"Unknown file type: {path}")
                unknown.append(str(path))

        
        logger.info(
            f"Scan complete: {len(images)} images, {len(texts)} texts, {len(unknown)} unknown"
        )

        return ScanResult(images, texts, unknown, errors)
    
        logger.info(f"Scanning folder: {input_dir}")
        logger.warning(f"Unknown file type: {path}")


