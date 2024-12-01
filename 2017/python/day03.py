import os
import common


def part1():
    real_file = os.path.join("..", "data", "day03_input.txt")
    data = common.get_file_contents(real_file)

    print(len(data))
    return "not complete"


def part2():
    # real_file = os.path.join("..", "data", "day03_input.txt")
    # data = common.get_file_contents(real_file)

    return "not complete"


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
