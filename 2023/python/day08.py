test_lines = ["LLR", "", "AAA = (BBB, BBB)", "BBB = (AAA, ZZZ)", "ZZZ = (ZZZ, ZZZ)"]

import common


def get_data(debug):
    if debug:
        data = test_lines
    else:
        data = common.get_file_contents("data/day08_input.txt")
    return data


def parse_lines(lines):
    result = {"directions": lines[0], "paths": {}}

    for line in lines[2:]:
        parts = line.split(" = ")
        dest_parts = parts[1].split(", ")

        result["paths"][parts[0]] = {"L": dest_parts[0][1:], "R": dest_parts[1][:3]}

    return result


def part1(debug=True):
    lines = get_data(debug)

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


def part2(debug=True):
    lines = get_data(debug)


if __name__ == "__main__":
    part1(False)
    part2()
