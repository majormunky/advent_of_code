import os
import common


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_lowest(row, col, data):
    # we need to see if the top, left, bottom, and right are lower than our val
    current_val = int(data[row][col])
    max_rows = len(data) - 1
    max_cols = len(data[0]) - 1

    result = True

    # check for up
    if row != 0:
        # we are not at the top row, we can check up
        up_val = int(data[row - 1][col])
        if up_val <= current_val:
            # we have a lower area
            result = False

    # check for left
    if col != 0:
        left_val = int(data[row][col - 1])
        if left_val <= current_val:
            result = False

    # check for right
    if col != max_cols:
        right_val = int(data[row][col + 1])
        if right_val <= current_val:
            result = False

    # check for down
    if row != max_rows:
        down_val = int(data[row + 1][col])
        if down_val <= current_val:
            result = False

    return result


def get_low_points(data):
    result = []
    for row_index, row in enumerate(data):
        for col_index, col in enumerate(row):
            if is_lowest(row_index, col_index, data):
                result.append([col_index, row_index])
    return result


def get_basin(low_point, data):
    result = []

    def get_node(x, y):
        try:
            return int(data[y][x])
        except IndexError:
            return False

    def fill(x, y):
        try:
            if data[y][x] == 9:
                return
        except IndexError:
            return

        if [x, y] in result:
            return

        if x < 0 or y < 0:
            return

        result.append([x, y])
        right = get_node(x + 1, y)
        if right and right < 9:
            fill(x + 1, y)

        left = get_node(x - 1, y)
        if left and left < 9:
            fill(x - 1, y)

        up = get_node(x, y - 1)
        if up and up < 9:
            fill(x, y - 1)

        down = get_node(x, y + 1)
        if down and down < 9:
            fill(x, y + 1)

    fill(*low_point)
    return result


def p1():
    real_file = os.path.join("..", "data", "day09_input.txt")
    lines = common.get_file_contents(real_file)

    result = 0
    for row_index, row in enumerate(lines):
        for col_index, col in enumerate(row):
            if is_lowest(row_index, col_index, lines):
                result += int(col) + 1

    return result


def p2():
    real_file = os.path.join("..", "data", "day09_input.txt")
    lines = common.get_file_contents(real_file)

    basins = []

    low_points = get_low_points(lines)
    for low_point in low_points:
        basin_points = get_basin(low_point, lines)
        basins.append(basin_points)

    # sort by length
    basins = sorted(basins, key=lambda x: len(x), reverse=True)

    answer = len(basins[0]) * len(basins[1]) * len(basins[2])
    return answer


if __name__ == "__main__":
    print("Part 1:", p1())
    print("Part 2:", p2())
