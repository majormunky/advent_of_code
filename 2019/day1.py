import os
from common import DATA_DIR, get_file_lines


def calculate_fuel_usage(amount):
    val = amount // 3
    return val - 2


def part1():
    """
    For the first part, we need to read in data from a text file
    each line is the amount of mass for something
    we need to calculate how much fuel that will take
    and then return the total
    """
    filepath = os.path.join(DATA_DIR, "day1-input.txt")
    lines = get_file_lines(filepath)
    total = 0
    for line in lines:
        total += calculate_fuel_usage(int(line))
    return total


def part2():
    """
    For part 2 we need to the same thing, but,
    we need to also calculate fuel for the fuel we are adding
    """
    filepath = os.path.join(DATA_DIR, "day1-input.txt")
    lines = get_file_lines(filepath)
    total = 0
    for line in lines:
        this_total = calculate_fuel_usage(int(line))
        while (this_total > 0):
            # each time we loop, the amount of fuel will decrease
            # until we hit zero, once that happens we're done
            total += this_total
            this_total = calculate_fuel_usage(this_total)
    return total

def main():
    print("Answer for Part 1: {}".format(part1()))
    print("Answer for Part 2: {}".format(part2()))

if __name__ == "__main__":
    main()