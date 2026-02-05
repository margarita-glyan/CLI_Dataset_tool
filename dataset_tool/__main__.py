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
    for img in result.images[:3]:
        print(f"   - {img.path.name} ({img.size_bytes} bytes)")

    print()

    print(f"📄 Texts: {len(result.texts)}")
    for txt in result.texts[:3]:
        print(f"   - {txt.path.name} ({txt.line_count()} lines)")

    print()

    print(f"❓ Unknown: {len(result.unknown)}")

    # ✅ Duplicate Detection inside scan
    if args.dupes:
        print("\n🔍 Duplicate Detection")
        print("=" * 30)

        from dataset_tool.core.duplicates import find_duplicates

        all_files = result.images + result.texts
        dupes = find_duplicates(all_files)

        if not dupes:
            print("No duplicates found ✅")
        else:
            print(f"Found {len(dupes)} duplicate groups:\n")
            for h, files in dupes.items():
                print(f"Hash: {h[:10]}...")
                for f in files:
                    print("  -", f.path.name)
                print()

    print("\n✅ Scan complete\n")


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

    # --- scan ---
    scan_parser = subparsers.add_parser("scan", help="Scan dataset folder")
    scan_parser.add_argument("path", help="Path to dataset folder")

    # ✅ flag must be added AFTER scan_parser exists
    scan_parser.add_argument(
        "--dupes",
        action="store_true",
        help="Detect duplicate files using SHA256",
    )

    scan_parser.set_defaults(func=run_scan)

    # --- organize ---
    organize_parser = subparsers.add_parser("organize", help="Organize dataset")
    organize_parser.set_defaults(func=run_organize)

    # --- manifest ---
    manifest_parser = subparsers.add_parser("manifest", help="Generate manifest")
    manifest_parser.set_defaults(func=run_manifest)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
