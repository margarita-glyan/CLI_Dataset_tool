import argparse
from pathlib import Path

from dataset_tool.core.scanner import Scanner


def run_scan(args) -> None:
    scanner = Scanner()
    result = scanner.scan(Path(args.path))

    print(f"Scanned: {args.path}")
    print(f"Images: {len(result.images)}")
    print(f"Texts: {len(result.texts)}")
    print(f"Unknown: {len(result.unknown)}")
    print(f"Errors: {len(result.errors)}")


def run_organize(args) -> None:
    print("ORGANIZE: not implemented yet")


def run_manifest(args) -> None:
    print("MANIFEST: not implemented yet")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="dataset-tool",
        description="Dataset organizer and analyzer for images and text",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    scan_parser = subparsers.add_parser("scan", help="Scan dataset folder")
    scan_parser.add_argument("path", help="Path to dataset folder")
    scan_parser.set_defaults(func=run_scan)

    organize_parser = subparsers.add_parser("organize", help="Organize dataset")
    organize_parser.set_defaults(func=run_organize)

    manifest_parser = subparsers.add_parser("manifest", help="Generate manifest")
    manifest_parser.set_defaults(func=run_manifest)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
