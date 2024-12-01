import os
import sys


DATA_DIR = os.path.join(".", "data")


def get_file_contents(filepath, single_line=False):
    lines = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            lines.append(line.strip())
    if single_line:
        return lines[0]
    return lines
