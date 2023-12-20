import itertools
import common


test_data = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#.....",
]

distance_tests = [
    (1, 2, 6),
    (1, 3, 6),
    (1, 4, 9),
    (1, 5, 9),
    (1, 6, 15),
    (1, 7, 15),
    (1, 8, 15),
    (1, 9, 12),
    (2, 3, 10),  # 11
    (2, 4, 5),
    (2, 5, 13),  # 14
    (2, 6, 9),  # 8
    (2, 7, 9),
    (2, 8, 19),  # 20
    (2, 9, 14),
    (3, 4, 11),
    (3, 5, 5),  # 4
    (3, 6, 17),
    (3, 7, 17),
    (3, 8, 9),
    (3, 9, 14),
    (4, 5, 8),  # 9
    (4, 6, 6),  # 5
    (4, 7, 6),  # 5
    (4, 8, 14),  # 154
    (4, 9, 9),
    (5, 6, 12),
    (5, 7, 12),
    (5, 8, 6),
    (5, 9, 9),
    (6, 7, 6),  # 4
    (6, 8, 16),  # 15
    (6, 9, 11),  # 9
    (7, 8, 10),  # 11
    (7, 9, 5),
    (8, 9, 5),
]


def get_data(debug, test_data):
    if debug:
        data = test_data
    else:
        data = common.get_file_contents("data/day11_input.txt")
    return data


def get_empty_paths(lines):
    result = {"rows": [], "cols": []}

    for y in range(len(lines)):
        is_empty = True
        for x in range(len(lines[0])):
            if lines[y][x] == "#":
                is_empty = False

        if is_empty:
            result["rows"].append(y)

    for x in range(len(lines[0])):
        is_empty = True
        for y in range(len(lines)):
            if lines[y][x] == "#":
                is_empty = False

        if is_empty:
            result["cols"].append(x)

    return result


def output_map(empty_data, lines, show_markers=False):
    if show_markers:
        header = ""
        for x in range(len(lines[0])):
            if x in empty_data["cols"]:
                print(x)
                header += "V"
            else:
                header += " "
        print(header)

    for line_index, line in enumerate(lines):
        output = ""
        output += line

        if show_markers:
            if line_index in empty_data["rows"]:
                output += "<"
            else:
                output += f"{line_index}"

        print(output)


def calculate_distance(g1_num, g2_num, map_data):
    x1, y1 = map_data[g1_num]
    x2, y2 = map_data[g2_num]

    result = abs(x1 - x2) + abs(y1 - y2)
    return result


def expand_space(empty_data, lines):
    empty_row = "." * len(lines[0])

    lines_added = 0
    for row_index in empty_data["rows"]:
        lines.insert(row_index + lines_added, empty_row)
        lines_added += 1

    # keep track of how many items we've added
    items_added = 0

    # go over each column that has an empty line
    for col_index in empty_data["cols"]:
        # go over each row
        for row_index in range(len(lines)):
            # break row into a list
            line_list = list(lines[row_index])

            # insert our new column into line
            current_index = col_index + items_added
            # print(f"Adding . at index {current_index} for row {row_index}")
            line_list.insert(col_index + items_added, ".")

            # increment how many we've added
            # items_added += 1

            # turn list back into a string
            line_string = "".join(line_list)

            # set our row to the new line string
            lines[row_index] = line_string

        # increment the items added after we've fixed all the rows
        items_added += 1

    return lines


def assign_numbers_to_galaxy(lines):
    result = {}

    i = 1

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "#":
                result[i] = (x, y)
                i += 1

    return result


def part1(debug=True):
    lines = get_data(debug, test_data)
    empty_data = get_empty_paths(lines)
    expanded_space = expand_space(empty_data, lines)
    galaxy_data = assign_numbers_to_galaxy(lines)
    galaxy_pairs = list(itertools.combinations(galaxy_data.keys(), 2))

    total = 0

    for gp in galaxy_pairs:
        dist = calculate_distance(gp[0], gp[1], galaxy_data)
        total += dist

    print(total)


def test_manhattan_distance(map_data):
    test_result = 0
    for d in distance_tests:
        test_result += d[2]
        dist = calculate_distance(d[0], d[1], map_data)
        if dist == d[2]:
            print("correct")
        else:
            print(f"incorrect {d}, wrong result: {dist}")


def part2(debug=True):
    lines = get_data(debug, test_data)


if __name__ == "__main__":
    part1(False)
    part2()
