import string
from common import get_file_contents


def get_line_parts(line):
    line_length = len(line) // 2
    left = line[:line_length]
    right = line[line_length:]
    return (left, right)


def get_priority_of_item_p1(item):
    letters = list(string.ascii_lowercase + string.ascii_uppercase)
    item_index = letters.index(item)
    return item_index + 1


def process_line_p1(line):
    left, right = get_line_parts(line)
    left_set = set(list(left))
    right_set = set(list(right))
    answer = left_set & right_set
    assert len(answer) == 1
    return list(answer)[0]


def get_groups_from_lines(lines):
    groups = []
    new_group = []

    for line in lines:
        new_group.append(line)
        if len(new_group) == 3:
            # add to groups and reset
            groups.append(new_group)
            new_group = []
    return groups


def get_common_item_from_group(group):
    first = set(group[0])
    second = set(group[1])
    third = set(group[2])
    result = first & second & third
    assert len(result) == 1
    return list(result)[0]


def p1():
    lines = get_file_contents("data/day03_input.txt")
    result = 0
    for line in lines:
        answer = process_line_p1(line)
        priority = get_priority_of_item_p1(answer)
        result += priority
    return result


def test_get_groups_from_lines():
    test_lines = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]
    groups = get_groups_from_lines(test_lines)
    assert len(groups) == 2


def p2():
    lines = get_file_contents("data/day03_input.txt")
    groups = get_groups_from_lines(lines)
    result = 0
    for group in groups:
        common_item = get_common_item_from_group(group)
        row_score = get_priority_of_item_p1(common_item)
        result += row_score
    return result


def main():
    print("Part 1: ", p1())
    print("Part 2: ", p2())


def tests():
    test_get_groups_from_lines()


if __name__ == "__main__":
    tests()
    main()
