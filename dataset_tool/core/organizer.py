import shutil
from pathlib import Path

from dataset_tool.core.scanner import Scanner


class Organizer:
    def organize(self, input_dir: Path, output_dir: Path) -> None:
        # 1) Scan input folder
        scanner = Scanner()
        result = scanner.scan(input_dir)

        # 2) Create output folders
        output_dir.mkdir(parents=True, exist_ok=True)

        images_dir = output_dir / "images"
        texts_dir = output_dir / "texts"
        unknown_dir = output_dir / "unknown"

        images_dir.mkdir(exist_ok=True)
        texts_dir.mkdir(exist_ok=True)
        unknown_dir.mkdir(exist_ok=True)

        # 3) Copy files
        for img in result.images:
            shutil.copy2(img.path, images_dir / img.path.name)

        for txt in result.texts:
            shutil.copy2(txt.path, texts_dir / txt.path.name)

        for u in result.unknown:
            src = Path(u)
            shutil.copy2(src, unknown_dir / src.name)

        print("✅ Dataset organized successfully!")
