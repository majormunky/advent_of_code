import os
import common


def part1():
    real_file = os.path.join("..", "data", "day01_input.txt")
    data = common.get_file_contents(real_file)

    answer = 0
    # loop over every entry
    for line in data:

        # for every entry, loop over the list again
        for line2 in data:

            left = int(line)
            right = int(line2)
            if left + right == 2020:
                answer = left * right
    return answer


def part2():
    real_file = os.path.join("..", "data", "day01_input.txt")
    data = common.get_file_contents(real_file)

    answer = 0
    for line in data:
        for line2 in data:
            for line3 in data:
                left = int(line)
                middle = int(line2)
                right = int(line3)
                if left + middle + right == 2020:
                    answer = left * middle * right
    return answer

def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
