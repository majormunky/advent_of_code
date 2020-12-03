import sys
import common
import math


def get_filename():
    filename = sys.argv[0]
    filename = filename.split("/")[-1]
    filename = filename.split(".")[0]
    return filename

data = common.get_file_contents("data/{}_input.txt".format(get_filename()))


def run_slop_test(right, down):
    field = []
    pos = [0, 0]
    tree_count = 0
    for row in data:
        field.append(list(row))
    while True:
        # check what the current spot is
        if field[pos[1]][pos[0]] == "#":
            # its a tree, increase our count
            tree_count += 1

            # for visuals, mark this as an x
            field[pos[1]][pos[0]] = "X"
        else:
            # we did not hit a tree
            # mark with a O for visuals
            field[pos[1]][pos[0]] = "O"

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

