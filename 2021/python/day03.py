import os
import common


def most_common(index, items, total):
    if int(items[index]) >= total / 2:
        return "1"
    else:
        return "0"


def least_common(index, items, total):
    # if our number is bigger than half our total lines
    # then we know that 1 is the more common value
    # so we return 0
    if int(items[index]) > total / 2:
        return "0"
    elif int(items[index]) == total / 2:
        return "0"
    else:
        return "1"


def build_frequency(lines):
    freq = [0 for i in range(len(lines[0]))]

    for line in lines:
        parts = list(line)
        for index, item in enumerate(parts):
            if item == "1":
                freq[index] += 1
    return freq


def p1():
    real_file = os.path.join("..", "data", "day03_input.txt")
    lines = common.get_file_contents(real_file)

    freq = build_frequency(lines)

    gamma = [most_common(i, freq, len(lines)) for i in range(len(freq))]
    epsilon = [least_common(i, freq, len(lines)) for i in range(len(freq))]
    gamma = int("0b" + "".join(gamma), 2)
    epsilon = int("0b" + "".join(epsilon), 2)
    return gamma * epsilon


def digit_check(index, number, target_value):
    return number[index] == target_value


def get_item(lines, func):
    data = lines.copy()
    freq = build_frequency(data)
    items_to_remove = []
    for index in range(len(data[0])):
        # num is either the most or least common number
        num = func(index, freq, len(data))
        for line in data:
            if not digit_check(index, line, num):
                if line in data:
                    items_to_remove.append(line)
        for remove_item in items_to_remove:
            if remove_item in data:
                data.remove(remove_item)
        if len(data) == 1:
            break

        freq = build_frequency(data)
    return data[0]


test_data = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def p2():
    real_file = os.path.join("..", "data", "day03_input.txt")
    lines = common.get_file_contents(real_file)

    oxygen = get_item(lines, most_common)
    scrubber = get_item(lines, least_common)

    return int("0b" + oxygen, 2) * int("0b" + scrubber, 2)


if __name__ == "__main__":
    print("Part 1: ", p1())
    print("Part 2: ", p2())
