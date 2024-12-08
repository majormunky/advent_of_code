import os
import common


def convert_line_to_ints(line):
    result = []
    parts = line.split(" ")
    for part in parts:
        result.append(int(part))
    return result


def compare_list(list1, list2):
    return all(x == y for x, y in zip(list1, list2))


def is_line_valid(num_list):
    is_valid = True
    last_num = None

    inc_list = sorted(num_list)
    dec_list = sorted(num_list, reverse=True)

    # check if list is all increasing or decreasing
    all_inc = compare_list(inc_list, num_list)
    all_dec = compare_list(dec_list, num_list)
    if not all_inc and not all_dec:
        is_valid = False

    for num in num_list:
        if last_num is None:
            last_num = num
        else:
            diff = abs(num - last_num)
            if diff < 1 or diff > 3:
                is_valid = False
            last_num = num
    return is_valid


def build_dumb_lists(num_list):
    result = []

    for i in range(len(num_list)):
        tmp_list = []
        for j in range(len(num_list)):
            if i != j:
                tmp_list.append(num_list[j])
        result.append(tmp_list)

    return result


def part1():
    real_file = os.path.join("..", "data", "day02_input.txt")
    lines = common.get_file_contents(real_file)

    answer = 0

    for line in lines:
        nums = convert_line_to_ints(line)
        if is_line_valid(nums):
            answer += 1

    print(answer)


def part2():
    real_file = os.path.join("..", "data", "day02_input.txt")
    lines = common.get_file_contents(real_file)

    answer = 0

    for line in lines:
        nums = convert_line_to_ints(line)
        if is_line_valid(nums):
            answer += 1
        else:
            test_lists = build_dumb_lists(nums)
            for t in test_lists:
                if is_line_valid(t):
                    answer += 1
                    break

    print(answer)


if __name__ == "__main__":
    part1()
    part2()
