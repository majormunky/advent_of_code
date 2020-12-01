import sys
import common
import collections


def get_filename():
    filename = sys.argv[0]
    filename = filename.split("/")[-1]
    filename = filename.split(".")[0]
    return filename

data = common.get_file_contents("data/{}_input.txt".format(get_filename()))


def part1():
    # setup list for each slot
    results = [
        [], [], [], [], [], [], [], []
    ]

    answer = ""

    # here we need to build up our lists
    for line in data:
        for index, character in enumerate(line):
            results[index].append(character)

    # now that the lists are complete, we can count them
    for index, slot in enumerate(results):
        # create a counter per slot
        counter = collections.Counter(slot)

        # grab the most common character and add it to our answer
        answer += counter.most_common(1)[0][0]

    return answer


def part2():
    return "not complete"


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
