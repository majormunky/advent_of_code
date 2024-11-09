import common


data = common.get_file_contents("data/day2_input.txt")


class Grid1:
    def __init__(self, width, height, current_pos):
        self.pad = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
        ]
        self.width = width
        self.height = height
        self.pos = current_pos

    def move_up(self):
        self.pos[1] -= 1
        if self.pos[1] < 0:
            self.pos[1] = 0

    def move_down(self):
        self.pos[1] += 1
        if self.pos[1] >= self.height:
            self.pos[1] = self.height - 1

    def move_left(self):
        self.pos[0] -= 1
        if self.pos[0] < 0:
            self.pos[0] = 0

    def move_right(self):
        self.pos[0] += 1
        if self.pos[0] >= self.width:
            self.pos[0] = self.width - 1

    def get_key(self):
        return self.pad[self.pos[1]][self.pos[0]]


class Grid2:
    def __init__(self, width, height, start_pos):
        self.width = width
        self.height = height
        self.pos = start_pos
        self.pad = [
            [None, None, "1", None, None],
            [None, "2", "3", "4", None],
            ["5", "6", "7", "8", "9"],
            [None, "A", "B", "C", None],
            [None, None, "D", None, None]
        ]

    def move_up(self):
        self.pos[1] -= 1
        if self.pos[1] < 0:
            self.pos[1] = 0
        if self.pad[self.pos[1]][self.pos[0]] is None:
            self.pos[1] += 1

    def move_down(self):
        self.pos[1] += 1
        if self.pos[1] >= self.height:
            self.pos[1] = self.height - 1
        if self.pad[self.pos[1]][self.pos[0]] is None:
            self.pos[1] -= 1

    def move_left(self):
        self.pos[0] -= 1
        if self.pos[0] < 0:
            self.pos[0] = 0
        if self.pad[self.pos[1]][self.pos[0]] is None:
            self.pos[0] += 1

    def move_right(self):
        self.pos[0] += 1
        if self.pos[0] >= self.width:
            self.pos[0] = self.width - 1
        if self.pad[self.pos[1]][self.pos[0]] is None:
            self.pos[0] -= 1

    def get_key(self):
        return self.pad[self.pos[1]][self.pos[0]]


def part1():
    pos = [1, 1]
    grid = Grid1(3, 3, pos)
    answer = ""

    for num_line in data:
        for direction in num_line:
            if direction == "U":
                grid.move_up()
            elif direction == "D":
                grid.move_down()
            elif direction == "L":
                grid.move_left()
            elif direction == "R":
                grid.move_right()
        answer += grid.get_key()
    return answer


def part2():
    pos = [0, 3]
    grid = Grid2(5, 5, pos)
    answer = ""

    for num_line in data:
        for direction in num_line:
            if direction == "U":
                grid.move_up()
            elif direction == "D":
                grid.move_down()
            elif direction == "L":
                grid.move_left()
            elif direction == "R":
                grid.move_right()
        answer += grid.get_key()
    return answer


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
