import os
import common


def get_pairs(item):
    item_min, item_max = item.split("-")
    return (int(item_min), int(item_max))


def get_test_lines():
    data = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]
    return data


def is_contained(first, second):
    first_min, first_max = get_pairs(first)
    second_min, second_max = get_pairs(second)

    result = False

    if first_min >= second_min and first_max <= second_max:
        result = True
    elif second_min >= first_min and second_max <= first_max:
        result = True
    return result


def p1():
    # 830 - too high
    # 404 - too low
    # 527 - No
    # 485 - Good

    real_file = os.path.join("..", "data", "day04_input.txt")
    lines = common.get_file_contents(real_file)

    count = 0
    for line in lines:
        first, second = line.split(",")
        if is_contained(first, second):
            count += 1
    print(count)


def is_overlap(first, second):
    first_min, first_max = get_pairs(first)
    second_min, second_max = get_pairs(second)

    result = False

    first_set = set(list(range(first_min, first_max + 1)))
    second_set = set(list(range(second_min, second_max + 1)))

    common = first_set & second_set

    if len(common) > 0:
        result = True

    return result


def p2():
    real_file = os.path.join("..", "data", "day04_input.txt")
    lines = common.get_file_contents(real_file)

    count = 0
    for line in lines:
        first, second = line.split(",")
        if is_overlap(first, second):
            count += 1
    print(count)


def main():
    p1()
    p2()


if __name__ == "__main__":
    main()
