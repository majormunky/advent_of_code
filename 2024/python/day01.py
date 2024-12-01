import os
import common
import collections


def get_file_data(filename):
    return common.get_file_contents(filename)


def get_lists(lines):
    left_list = []
    right_list = []

    for i in lines:
        parts = i.split(" ")
        left_list.append(int(parts[0]))
        right_list.append(int(parts[-1]))

    return left_list, right_list


def part1():
    real_file = os.path.join(common.DATA_DIR, "day01_input.txt")
    test_file = os.path.join(common.DATA_DIR, "day01_sample.txt")
    lines = get_file_data(real_file)
    left_list, right_list = get_lists(lines)

    # sort the lists
    left_list = sorted(left_list)
    right_list = sorted(right_list)

    total = 0

    for i in range(len(left_list)):
        diff = abs(left_list[i] - right_list[i])
        total += diff

    print(total)


def part2():
    real_file = os.path.join(common.DATA_DIR, "day01_input.txt")
    test_file = os.path.join(common.DATA_DIR, "day01_sample.txt")
    lines = get_file_data(real_file)
    left_list, right_list = get_lists(lines)

    right_list_data = collections.Counter(right_list)

    total = 0

    for num in left_list:
        score = num * right_list_data[num]
        total += score

    print(total)



if __name__ == "__main__":
    part1()
    part2()
