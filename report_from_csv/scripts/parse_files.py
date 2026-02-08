import csv
from pathlib import Path


def parse_files(files: list[str]):
    result = []
    for filename in files:
        with open(Path(filename)) as f:
            data = csv.DictReader(f)
            result.extend(data)
    return result