from pathlib import Path


def read_from_file(infile):
    return Path(infile).read_text(encoding="utf-8")
