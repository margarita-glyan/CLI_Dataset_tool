from pathlib import Path
from dataset_tool.core.organizer import Organizer


def test_organize_creates_folders(tmp_path):
    organizer = Organizer()
    organizer.organize(Path("tests/sample_data"), tmp_path)

    assert (tmp_path / "images").exists()
    assert (tmp_path / "texts").exists()
    assert (tmp_path / "unknown").exists()
