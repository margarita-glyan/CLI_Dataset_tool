import json
from pathlib import Path

from dataset_tool.core.scanner import Scanner


def generate_manifest(input_dir: Path, output_file: Path) -> None:
    scanner = Scanner()
    result = scanner.scan(input_dir)

    manifest = {
        "images": [],
        "texts": [],
        "unknown": result.unknown,
        "errors": result.errors,
    }

    # Images
    for img in result.images:
        manifest["images"].append(
            {
                "name": img.path.name,
                "size_bytes": img.size_bytes,
                "sha256": img.sha256,
            }
        )

    # Texts
    for txt in result.texts:
        manifest["texts"].append(
            {
                "name": txt.path.name,
                "size_bytes": txt.size_bytes,
                "lines": txt.line_count(),
                "sha256": txt.sha256,
            }
        )

    # Save JSON
    output_file.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"✅ Manifest saved to {output_file}")
