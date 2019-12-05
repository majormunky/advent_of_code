import os
from common import DATA_DIR, get_file_lines


def calculate_fuel_usage(amount):
    val = amount // 3
    return val - 2


def main():
    filepath = os.path.join(DATA_DIR, "day1-input.txt")
    lines = get_file_lines(filepath)
    total = 0
    for line in lines:
        total += calculate_fuel_usage(int(line))
    print(total)


def main2():
    filepath = os.path.join(DATA_DIR, "day1-input.txt")
    lines = get_file_lines(filepath)
    total = 0
    for line in lines:
        this_total = calculate_fuel_usage(int(line))
        while (this_total > 0):
            total += this_total
            this_total = calculate_fuel_usage(this_total)
    print(total)


if __name__ == "__main__":
    main2()