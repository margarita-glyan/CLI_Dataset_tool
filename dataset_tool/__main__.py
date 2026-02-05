import argparse
from pathlib import Path

from dataset_tool.core.scanner import Scanner


def run_scan(args) -> None:
    scanner = Scanner()
    result = scanner.scan(Path(args.path))

    print("\n📂 Scan Summary")
    print("=" * 30)
    print(f"Scanned folder: {args.path}")
    print(f"Total files: {result.total_files}")
    print()

    print(f"🖼 Images: {len(result.images)}")
    print(f"📄 Texts: {len(result.texts)}")
    print(f"❓ Unknown: {len(result.unknown)}")

    if args.dupes:
        from dataset_tool.core.duplicates import find_duplicates

        print("\n🔍 Duplicate Detection")
        dupes = find_duplicates(result.images + result.texts)

        if not dupes:
            print("No duplicates found ✅")
        else:
            print(f"Found {len(dupes)} duplicate groups:")
            for h, files in dupes.items():
                print(f"Hash: {h[:10]}...")
                for f in files:
                    print("  -", f.path.name)

    print("\n✅ Scan complete\n")


def run_organize(args) -> None:
    from dataset_tool.core.organizer import Organizer

    organizer = Organizer()
    organizer.organize(Path(args.input_dir), Path(args.output_dir))


    organizer = Organizer()
    organizer.organize(Path(args.input_dir), Path(args.output_dir))


def run_manifest(args) -> None:
    print("MANIFEST: not implemented yet")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="dataset-tool",
        description="Dataset organizer and analyzer for images and text",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # ---- scan ----
    scan_parser = subparsers.add_parser("scan", help="Scan dataset folder")
    scan_parser.add_argument("path", help="Path to dataset folder")
    scan_parser.add_argument(
        "--dupes",
        action="store_true",
        help="Detect duplicate files",
    )
    scan_parser.set_defaults(func=run_scan)

    # ---- organize ----
    organize_parser = subparsers.add_parser("organize", help="Organize dataset")
    organize_parser.add_argument("input_dir", help="Input dataset folder")
    organize_parser.add_argument("output_dir", help="Output folder")
    organize_parser.set_defaults(func=run_organize)

    # ---- manifest ----
    manifest_parser = subparsers.add_parser("manifest", help="Generate manifest")
    manifest_parser.set_defaults(func=run_manifest)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
