from pathlib import Path
from dataset_tool.core.scanner import Scanner


def test_scan_sample_data():
    scanner = Scanner()
    result = scanner.scan(Path("tests/sample_data"))

    assert len(result.images) == 3
    assert len(result.texts) == 2
    assert len(result.unknown) == 1
