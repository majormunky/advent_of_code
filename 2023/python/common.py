import os


DATA_DIR = os.path.join(".", "data")


def get_file_contents(filepath, single_line=False, strip_line=True):
    lines = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            if strip_line:
                line = line.strip()
            lines.append(line)
    if single_line:
        return lines[0]
    return lines
