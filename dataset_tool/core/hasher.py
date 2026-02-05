import hashlib
from pathlib import Path


def file_sha256(path: Path) -> str:
    """
    Compute SHA256 hash of a file.
    Reads in chunks (safe for large files).
    """
    sha = hashlib.sha256()

    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha.update(chunk)

    return sha.hexdigest()
