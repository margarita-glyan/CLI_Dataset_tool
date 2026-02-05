from collections import defaultdict

from dataset_tool.models.media_file import MediaFile


def find_duplicates(files: list[MediaFile]) -> dict[str, list[MediaFile]]:
    """
    Group files by sha256 hash.
    Returns only hashes that have more than 1 file.
    """
    groups = defaultdict(list)

    for f in files:
        groups[f.sha256].append(f)

    return {h: fs for h, fs in groups.items() if len(fs) > 1}
