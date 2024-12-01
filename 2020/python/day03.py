import os
import common
import math


def run_slop_test(right, down):
    real_file = os.path.join("..", "data", "day01_input.txt")
    data = common.get_file_contents(real_file)

    # holds the map we will navigate
    field = []

    # current position on the map
    pos = [0, 0]

    # how many trees have we hit?
    tree_count = 0

    # build our field
    for row in data:
        field.append(list(row))

    while True:
        # check what the current spot is
        if field[pos[1]][pos[0]] == "#":
            # its a tree, increase our count
            tree_count += 1

        # increase our position further down the field
        pos[0] += right
        pos[1] += down

        # if we reached the right side of the field
        # then we reset our position back to the start
        if pos[0] >= len(field[0]):
            pos[0] = pos[0] - len(field[0])

        # if we've reached the bottom of the field, we are done
        if pos[1] >= len(field):
            break

    return tree_count


def part1():
    # real_file = os.path.join("..", "data", "day01_input.txt")
    # data = common.get_file_contents(real_file)

    return run_slop_test(3, 1)


def part2():
    slope_tests = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    answers = []
    for slope in slope_tests:
        answers.append(run_slop_test(slope[0], slope[1]))

    return math.prod(answers)


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
