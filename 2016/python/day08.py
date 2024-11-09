import common
import sys

def get_filename():
    filename = sys.argv[0]
    filename = filename.split("/")[-1]
    filename = filename.split(".")[0]
    return filename

data = common.get_file_contents("data/{}_input.txt".format(get_filename()))
test_data = [
    "rect 3x2",
    "rotate column x=1 by 1",
    "rotate row y=0 by 4",
    "rotate column x=1 by 1"
]


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        self.build_grid()

    def build_grid(self):
        self.cells = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(0)
            self.cells.append(row)

    def fill_rect(self, width, height):
        for y in range(height):
            for x in range(width):
                self.cells[y][x] = 1

    def clear_column(self, col_num):
        for y in range(self.height):
            self.cells[y][col_num] = 0

    def clear_row(self, row_num):
        for x in range(self.width):
            self.cells[row_num][x] = 0

    def output(self):
        output = []
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                cell = self.cells[y][x]
                if cell == 0:
                    row += "."
                else:
                    row += "#"
            output.append(row)

        for row in output:
            print(row)

    def rotate_column(self, column, amount):
        column_cells = self.get_column(column)
        shifted_cells = self.shift_list(column_cells, amount)

        self.clear_column(column)

        cell_index = 0
        for y in range(self.height):
            self.cells[y][column] = shifted_cells[cell_index]
            cell_index += 1

    def rotate_row(self, row, amount):
        row_cells = self.cells[row]
        shifted_cells = self.shift_list(row_cells, amount)
        self.clear_row(row)
        row_index = 0
        for x in range(self.width):
            self.cells[row][x] = shifted_cells[row_index]
            row_index += 1

    def apply(self, instruction):
        if instruction["type"] == "rect":
            self.fill_rect(instruction["width"], instruction["height"])
        elif instruction["rotate_direction"] == "column":
            self.rotate_column(instruction["start_pos"], instruction["amount"])
        else:
            self.rotate_row(instruction["start_pos"], instruction["amount"])

    def get_column(self, col_num):
        result = []
        for y in range(self.height):
            result.append(self.cells[y][col_num])
        return result

    def shift_list(self, cell_list, amount):
        print(cell_list)
        new_list = [0 for x in range(len(cell_list))]

        current_index = amount

        for i in range(len(cell_list)):
            if current_index >= len(cell_list):
                current_index = 0

            # print("Current Index:", current_index)
            new_list[current_index] = cell_list[i]
            current_index += 1

        return new_list

    def count_cells(self):
        result = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.cells[y][x] == 1:
                    result += 1
        return result


def parse_instruction(inst: str) -> dict:
    parts = inst.split(" ")
    result = None

    if parts[0] == "rect":
        size_parts = parts[1].split("x")
        width = int(size_parts[0])
        height = int(size_parts[1])
        result = {"type": "rect", "width": width, "height": height}
    else:
        rotate_amount = parts[2].split("=")
        rotate_value = int(parts[-1])
        rotate_start = int(rotate_amount[1])
        result = {"type": "rotate", "rotate_direction": parts[1], "amount": rotate_value, "start_pos": rotate_start}

    return result


def build_instructions(data):
    result = []
    for line in data:
        result.append(parse_instruction(line))
    return result


def part1():
    width = 50
    height = 6
    grid = Grid(width, height)
    instructions = build_instructions(data)

    for i in instructions:
        print(i)
        grid.apply(i)

    grid.output()
    result = grid.count_cells()
    return result

def main():
    p1 = part1()

    print("Part 1", p1)


if __name__ == "__main__":
    main()
