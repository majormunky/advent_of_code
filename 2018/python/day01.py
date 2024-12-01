import os
import common
import itertools





def part1():
    real_file = os.path.join("..", "data", "day01_input.txt")
    data = common.get_file_contents(real_file)

    answer = 0
    for row in data:
        if "-" in row:
            answer -= int(row[1:])
        else:
            answer += int(row[1:])
    return answer


def part2():
    real_file = os.path.join("..", "data", "day01_input.txt")
    data = common.get_file_contents(real_file)

    frequency = 0
    seen_frequencies = []

    for row in itertools.cycle(data):
        freq_number = int(row[1:])

        if "-" in row:
            frequency -= freq_number
        else:
            frequency += freq_number

        if frequency in seen_frequencies:
            return frequency
        else:
            seen_frequencies.append(frequency)

    print(len(seen_frequencies))


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == "__main__":
    main()
