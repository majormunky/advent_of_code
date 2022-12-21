import os
import sys
import math
from common import get_file_contents

DEBUG = True
BOARD_WIDTH = 6
BOARD_HEIGHT = 5
SPEED = 0.75


def print_message(msg):
    if DEBUG:
        print(msg)


class Point:
    def __init__(self, x, y, icon):
        self.x = int(x)
        self.y = int(y)
        self.icon = icon
        self.parent = None
        self.child = None
        self.visited_tiles = set()
        self.visited_tiles.add((self.x, self.y))

    def add_child(self, other):
        self.child = other

    def add_parent(self, other):
        self.parent = other

    def move(self, direction_list):
        for direction in direction_list:
            match direction:
                case "north":
                    self.y += 1
                case "south":
                    self.y -= 1
                case "east":
                    self.x += 1
                case "west":
                    self.x -= 1
        self.visited_tiles.add((self.x, self.y))

    def distance_to(self, other):
        x_diff = other.x - self.x
        y_diff = other.y - self.y
        float_dist = math.sqrt(x_diff ** 2 + y_diff ** 2)
        return int(float_dist)

    def is_at(self, x, y):
        return self.x == x and self.y == y

    def direction_to(self, other):
        if self.is_at(other.x, other.y):
            return None

        if self.x == other.x and self.y < other.y:
            return ["north"]
        elif self.x == other.x and self.y > other.y:
            return ["south"]
        elif self.y == other.y and self.x > other.x:
            return ["west"]
        elif self.y == other.y and self.x < other.x:
            return ["east"]
        elif self.x > other.x and self.y < other.y:
            return ["north", "west"]
        elif self.x < other.x and self.y < other.y:
            return ["north", "east"]
        elif self.x > other.x and self.y > other.y:
            return ["south", "west"]
        elif self.x < other.x and self.y > other.y:
            return ["south", "east"]


def render_board(width, height, start, head, tail):
    lines = []

    for y in range(height):
        line = ""

        for x in range(width):
            if head.is_at(x, y):
                line += "H"
            elif tail.is_at(x, y):
                line += "T"
            elif start.is_at(x, y):
                line += "s"
            else:
                line += "."
        lines.append(line)

    lines.append(f"Tail: {tail.x}, {tail.y}\n")
    lines.append(f"Head: {head.x}, {head.y}\n")

    return "\n".join(reversed(lines))


def render_board_p2(width, height, start, head):
    lines = []
    for y in range(height):
        line = ""
        for x in range(width):
            line += "."
        lines.append(line)

    node = head
    while True:
        # print(node.icon, node.x, node.y)
        line_list = list(lines[node.y])
        line_list[node.x] = node.icon
        lines[node.y] = "".join(line_list)
        if not node.child:
            break
        node = node.child

    return "\n".join(reversed(lines))


def process_line(line, start, head, tail):
    frames = []
    current_direction, amount = line.split(" ")
    steps_left = int(amount)
    direction_map = {
        "L": "west",
        "R": "east",
        "U": "north",
        "D": "south"
    }

    for step in range(steps_left):
        step_direction = direction_map[current_direction]
        head.move([step_direction])

        tail_distance = head.distance_to(tail)
        direction_to_head = []
        if tail_distance > 1:
            direction_to_head = tail.direction_to(head)
            tail.move(direction_to_head)

        frames.append({
            "frame": render_board(
                BOARD_WIDTH,
                BOARD_HEIGHT,
                start,
                head,
                tail,
            ),
            "tail_direction": direction_to_head,
            "line": line
        })
    return frames


def p1():
    lines = get_file_contents("data/day09_input.txt")
    # print_message(len(lines))

    head = Point(0, 0)
    tail = Point(0, 0)
    start = Point(0, 0)

    frames = [{
        "frame": render_board(BOARD_WIDTH, BOARD_HEIGHT, start, head, tail),
        "line": "",
        "tail_direction": "",
    }]

    for line in lines:
        frames.extend(process_line(line, start, head, tail))

    # display_visited_tiles(tail.visited_tiles)
    print(len(tail.visited_tiles))


def display_frames(frame_list):
    current_frame = 0

    while True:
        try:
            frame_to_display = frame_list[current_frame]
            display_frame(frame_to_display)
        except IndexError:
            pass
        next_input = input("Press <return> for next frame, or > for previous frame: ")
        print("Next Input: ", next_input)
        if next_input == "<":
            if current_frame > 0:
                current_frame -= 1
        elif next_input == "":
            if current_frame < len(frame_list):
                current_frame += 1


def display_visited_tiles(tile_list):
    grid = []
    for y in range(BOARD_HEIGHT):
        line = ""
        for x in range(BOARD_WIDTH):
            if (x, y) in tile_list:
                line += "#"
            else:
                line += "."
        grid.append(line)

    for line in reversed(grid):
        print(line)


def display_frame(frame):
    os.system("clear")
    sys.stdout.write(f">>--- {frame['line']} ---<<\n")
    sys.stdout.write(frame["frame"])
    sys.stdout.write("\n")
    sys.stdout.flush()


def p2():
    test_lines = [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2"
    ]
    
    test_lines2 = [
        "R 5",
        "U 8",
        "L 8",
        "D 3",
        "R 17",
        "D 10",
        "L 25",
        "U 20",
    ]

    lines = get_file_contents("data/day09_input.txt")

    frames = []

    nodes_to_create = 8
    start = Point(100, 100, "s")    
    head = Point(start.x, start.y, "H")
    tail = head

    board_size = 400

    while nodes_to_create >= 0:
        if nodes_to_create == 0:
            new_node = Point(start.x, start.y, "T")
        else:
            new_node = Point(start.x, start.y, str(nodes_to_create))
        tail.add_child(new_node)
        new_node.add_parent(tail)
        tail = new_node
        nodes_to_create -= 1

    current_node = head

    # frames.append(
    #     {
    #         "frame": render_board_p2(board_size, board_size, start, head),
    #         "line": ""
    #     }
    # )

    for line in lines:
        current_direction, amount = line.split(" ")
        steps_left = int(amount)
        direction_map = {
            "L": "west",
            "R": "east",
            "U": "north",
            "D": "south"
        }

        for step in range(steps_left):
            step_direction = direction_map[current_direction]
            head.move([step_direction])
            # frames.append(
            #     {
            #         "frame": render_board_p2(board_size, board_size, start, head),
            #         "line": ""
            #     }
            # )
            current_node = head.child
            while current_node:
                parent_distance = current_node.distance_to(current_node.parent)
                if parent_distance > 1:
                    parent_direction = current_node.direction_to(current_node.parent)
                    current_node.move(parent_direction)
                if not current_node.child:
                    break
                current_node = current_node.child
            # frames.append(
            #     {
            #         "frame": render_board_p2(board_size, board_size, start, head),
            #         "line": ""
            #     }
            # )

    # display_frames(frames)
    print(len(tail.visited_tiles))

    
def main():
    p2()


if __name__ == "__main__":
    main()
