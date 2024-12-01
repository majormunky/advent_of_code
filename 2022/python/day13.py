import os
import common
import ast


def get_data(debug):
    if debug:
        filepath = os.path.join("..", "data", "day13_test.txt")
        data = common.get_file_contents(filepath)
    else:
        filepath = os.path.join("..", "data", "day13_test.txt")
        data = common.get_file_contents(filepath)
    return data


def compare_lists(list1, list2):
    for left_index, left in enumerate(list1):
        right = list2[left_index]
        left_type = type(left)
        right_type = type(right)
        print(f"  - Compare {left} vs {right}")
        if left_type == int and right_type == int:
            if left < right:
                print("    - Left side is smaller")
                return True

            if right > left:
                print("    - Right side is smaller")
                return False
        elif left_type == list and right_type == list:
            return compare_lists(left, right)
        elif left_type == int and right_type == list:
            return compare_lists([left], right)
        elif left_type == list and right_type == int:
            return compare_lists(left, [right])


    return True


def part1(debug=True):
    lines = get_data(debug)
    data = []

    temp_line = None

    for line in lines:
        if line == "":
            continue

        if temp_line is None:
            temp_line = line
        else:
            data.append([
                ast.literal_eval(temp_line),
                ast.literal_eval(line)
            ])
            temp_line = None

    result = {}
    for index, item in enumerate(data):

        list1 = item[0]
        list2 = item[1]

        result[index] = compare_lists(list1, list2)
        print("")


def part2(debug=True):
    # lines = get_data(debug)
    return 0


if __name__ == "__main__":
    part1()
    part2()
