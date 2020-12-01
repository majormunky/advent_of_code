from dataclasses import dataclass
import common


@dataclass
class Point:
    x: int
    y: int


class Line:
    start: Point
    end: Point

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Line(start={self.start}, end={self.end})"

    def get_intersection_point(self, other):
        if other.x > start.x and other.x < end.x:
            if other.y > start.y and other.y < end.y:
                print("Intersects")
                return


def get_new_direction(current, left_or_right):
    dirs = {
        "N": {
            "L": "W",
            "R": "E"
        },
        "W": {
            "L": "S",
            "R": "N"
        },
        "S": {
            "L": "E",
            "R": "W"
        },
        "E": {
            "L": "N",
            "R": "S"
        }
    }
    return dirs[current][left_or_right]


def check_for_collisions(new_line, line_list):
    for line in line_list:
        if new_line.get_intersection_point(line):
            print("intersects")


def part1():
    # get input data
    data = common.get_file_contents("data/day1_input.txt", single_line=True)

    # set our intial position
    x = 0
    y = 0

    # and our current direction
    current_direction = "N"

    # loop over every instruction
    for instruction in data.split(","):
        # split up our instruction into its parts
        instruction = instruction.strip()
        side = instruction[:1]
        steps = int(instruction[1:])

        # Based on our current direction and our turn
        # what is our new direction?
        new_direction = get_new_direction(current_direction, side)

        # Now that we have our direction and steps
        # adjust our x and y positions
        if new_direction == "N":
            y += steps
        elif new_direction == "W":
            x -= steps
        elif new_direction == "E":
            x += steps
        elif new_direction == "S":
            y -= steps

        # and set our new current position
        current_direction = new_direction

    # we can just return x + y as our origin is 0, 0
    return x + y


def part2():
    data = common.get_file_contents("data/day1_input.txt", single_line=True)
    x = 0
    y = 0
    current_direction = "N"
    points = []

    points.append(Point(0, 0))

    for instruction in data.split(","):
        instruction = instruction.strip()
        side = instruction[:1]
        steps = int(instruction[1:])

        new_direction = get_new_direction(current_direction, side)
        if new_direction == "N":
            y += steps
        elif new_direction == "W":
            x += steps
        elif new_direction == "E":
            x -= steps
        elif new_direction == "S":
            y -= steps

        points.append(Point(x, y))


def main():
    part1_answer = part1()
    # part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    # print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
