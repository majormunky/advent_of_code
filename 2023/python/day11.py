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


class Grid:
    def __init__(self, lines):
        self.lines = lines
        self.height = len(lines)
        self.width = len(lines[0])
        self.empty_rows = self.identify_empty_rows()
        self.empty_cols = self.identify_empty_cols()
        self.galaxy_data = {}
        self.distance_data = None
        self.assign_numbers_to_galaxy()

    def assign_numbers_to_galaxy(self):
        self.galaxy_data = {}

        i = 1
        for y in range(self.height):
            for x in range(self.width):
                if self.lines[y][x] == "#":
                    key = (x, y)
                    self.galaxy_data[key] = i
                    i += 1

    def identify_empty_rows(self):
        result = []
        for y in range(self.height):
            is_empty = True
            for x in range(self.width):
                if self.lines[y][x] == "#":
                    is_empty = False

            if is_empty:
                result.append(y)
        return result

    def identify_empty_cols(self):
        result = []
        for x in range(self.width):
            is_empty = True
            for y in range(self.height):
                if self.lines[y][x] == "#":
                    is_empty = False

            if is_empty:
                result.append(x)
        return result

    def expand_rows(self, times):
        empty_row = "." * self.width

        lines_added = 0
        for row_index in self.empty_rows:
            extra_to_add = 0

            while True:
                extra_to_add += 1
                if extra_to_add >= times:
                    break
                self.lines.insert(row_index + lines_added, empty_row)
                lines_added += 1

        self.height = len(self.lines)

    def add_column(self, index):
        for row_index in range(self.height):
            row_list = list(self.lines[row_index])
            row_list.insert(index, ".")
            row_string = "".join(row_list)
            self.lines[row_index] = row_string
        self.width = len(self.lines[0])

    def expand_cols(self, times):
        new_cols = 0
        for col_index in self.empty_cols:
            for i in range(times - 1):
                self.add_column(col_index + new_cols)
                new_cols += 1

    def expand(self, times=1):
        self.expand_rows(times)
        self.expand_cols(times)
        self.assign_numbers_to_galaxy()

    def calculate_distance(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x1 - x2) + abs(y1 - y2)

    def calculate_distances(self):
        result = {}
        galaxy_numbers = itertools.combinations(self.galaxy_data.values(), 2)
        galaxy_lookup = {}

        for k, v in self.galaxy_data.items():
            galaxy_lookup[v] = k

        for pair in galaxy_numbers:
            galaxy_1 = galaxy_lookup[pair[0]]
            galaxy_2 = galaxy_lookup[pair[1]]

            result[pair] = self.calculate_distance(galaxy_1, galaxy_2)

        self.distance_data = result

    def output(self, show_markers=False):
        output = []
        if show_markers:
            header = []
            for x in range(self.width):
                if x in self.empty_cols:
                    header.append("V")
                else:
                    header.append(" ")
            output.append(header)

        for line_index, line in enumerate(self.lines):
            output_line = []

            for char in line:
                output_line.append(char)

            if show_markers:
                if line_index in self.empty_rows:
                    output_line.append("<")
                else:
                    output_line.append(f"{line_index}")
            output.append(output_line)

        for pos, num in self.galaxy_data.items():
            x, y = pos
            output[y][x] = str(num)

        for line in output:
            print("".join(line))


def get_data(debug, test_data):
    if debug:
        data = list(test_data)
    else:
        data = common.get_file_contents("../data/day11_input.txt")
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


# def output_map(empty_data, lines, show_markers=False):
#     if show_markers:
#         header = ""
#         for x in range(len(lines[0])):
#             if x in empty_data["cols"]:
#                 print(x)
#                 header += "V"
#             else:
#                 header += " "
#         print(header)

#     for line_index, line in enumerate(lines):
#         output = ""
#         output += line

#         if show_markers:
#             if line_index in empty_data["rows"]:
#                 output += "<"
#             else:
#                 output += f"{line_index}"

#         print(output)


def calculate_distance(g1_num, g2_num, map_data):
    x1, y1 = map_data[g1_num]
    x2, y2 = map_data[g2_num]

    result = abs(x1 - x2) + abs(y1 - y2)
    return result


def expand_space(empty_data, lines, amount_to_add=1):
    # print(
    #     f"Empty Rows {len(empty_data['rows'])} * {amount_to_add} = {len(empty_data['rows']) * amount_to_add}"
    # )
    # print(
    #     f"Empty Cols {len(empty_data['cols'])} * {amount_to_add} = {len(empty_data['cols']) * amount_to_add}"
    # )
    # print(f"Lines Before: {len(lines)}")
    empty_row = "." * len(lines[0])

    lines_added = 0
    for row_index in empty_data["rows"]:
        extra_to_add = 0

        while True:
            lines.insert(row_index + lines_added, empty_row)
            lines_added += 1
            extra_to_add += 1
            if extra_to_add >= amount_to_add:
                break

    # print("Lines Added:", lines_added)
    # print(f"Lines After: {len(lines)}")

    # keep track of how many items we've added
    items_added = 0

    # print(f"Columns Before: {len(lines[0])}")
    # go over each column that has an empty line
    for col_index in empty_data["cols"]:
        # print("Working on col index", col_index)
        # go over each row
        extra_to_add = 0

        # print("About to start while loop")
        while True:
            for row_index in range(len(lines)):
                # break row into a list
                line_list = list(lines[row_index])

                # insert our new column into line
                current_index = col_index + items_added
                # print(f"   Add item at col {current_index} row {row_index}")
                # print(f"Adding . at index {current_index} for row {row_index}")
                line_list.insert(current_index, ".")

                # increment how many we've added
                # items_added += 1

                # turn list back into a string
                line_string = "".join(line_list)

                # set our row to the new line string
                lines[row_index] = line_string

                # print("   Done adding item to row index", row_index)

            # increment the items added
            items_added += 1
            # print("Added items is now", items_added)

            # after we've added the new column
            # increment the amount of times we've done this
            extra_to_add += 1
            # print("Exra to add is now", extra_to_add)

            # check to see if we have added the right amount
            # of columns, if so, break out of this column
            if extra_to_add >= amount_to_add:
                # print("Added enough columns, breaking")
                break

    # print(f"Columns Added: {items_added}")
    # print(f"Columns After: {len(lines[0])}")

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
    expanded_space = expand_space(empty_data, lines, amount_to_add=1)
    galaxy_data = assign_numbers_to_galaxy(lines)
    galaxy_pairs = list(itertools.combinations(galaxy_data.keys(), 2))

    total = 0

    # for line in lines:
    #     print(line)

    for gp in galaxy_pairs:
        dist = calculate_distance(gp[0], gp[1], galaxy_data)
        # print(gp, dist)
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
    lines1 = get_data(debug, test_data)
    lines2 = get_data(debug, test_data)

    grid1 = Grid(lines1)
    grid2 = Grid(lines2)

    grid1.expand(times=1)
    grid2.expand(times=2)

    grid1.calculate_distances()
    grid2.calculate_distances()

    g1_value = sum(grid1.distance_data.values())
    g2_value = sum(grid2.distance_data.values())

    total = (g2_value - g1_value) * 999998 + 9608724

    print(total)


if __name__ == "__main__":
    part1(False)  # 9608724
    part2(False)  # 904633799472
