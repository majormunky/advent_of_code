import math
import sys
import time
import json

test_lines = ["LLR", "", "AAA = (BBB, BBB)", "BBB = (AAA, ZZZ)", "ZZZ = (ZZZ, ZZZ)"]
test_lines_2 = [
    "LR",
    "",
    "11A = (11B, XXX)",
    "11B = (XXX, 11Z)",
    "11Z = (11B, XXX)",
    "22A = (22B, XXX)",
    "22B = (22C, 22C)",
    "22C = (22Z, 22Z)",
    "22Z = (22B, 22B)",
    "XXX = (XXX, XXX)",
]


import common


def get_data(debug, test_data):
    if debug:
        return test_data
    else:
        return common.get_file_contents("data/day08_input.txt")


def parse_lines(lines):
    result = {"directions": lines[0], "paths": {}}

    for line in lines[2:]:
        parts = line.split(" = ")
        dest_parts = parts[1].split(", ")

        result["paths"][parts[0]] = {"L": dest_parts[0][1:], "R": dest_parts[1][:3]}

    return result


def part1(debug=True):
    lines = get_data(debug, test_lines)

    data = parse_lines(lines)

    # print(data)

    current_node = "AAA"
    steps = 0
    while True:
        for direction in data["directions"]:
            steps += 1
            current_node = data["paths"][current_node][direction]
            if current_node == "ZZZ":
                break
        if current_node == "ZZZ":
            break

    print(steps)


def find_steps(key, directions, paths):
    steps = 0

    current_value = key
    while True:
        for direction in directions:
            steps += 1
            current_value = paths[current_value][direction]
            if current_value.endswith("Z"):
                return steps


def part2(debug=True):
    lines = get_data(debug, test_lines_2)
    puzzle_data = parse_lines(lines)

    directions = puzzle_data["directions"]
    paths = puzzle_data["paths"]

    result = {}

    nodes = {}

    for key in puzzle_data["paths"].keys():
        if key.endswith("A"):
            nodes[key] = key

    for k, v in nodes.items():
        result[k] = find_steps(k, directions, paths)

    step_list = result.values()

    print(math.lcm(*step_list))


if __name__ == "__main__":
    part1(False)
    part2(False)
