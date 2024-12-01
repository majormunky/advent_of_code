import itertools
import common


test_data = ["..F7.", ".FJ|.", "SJ.L7", "|F--J", "LJ..."]


test_data_2 = [
    "...........",
    ".S-------7.",
    ".|F-----7|.",
    ".||.....||.",
    ".||.....||.",
    ".|L-7.F-J|.",
    ".|..|.|..|.",
    ".L--J.L--J.",
    "...........",
]


test_data_3 = [
    ".F----7F7F7F7F-7....",
    ".|F--7||||||||FJ....",
    ".||.FJ||||||||L7....",
    "FJL7L7LJLJ||LJ.L-7..",
    "L--J.L7...LJS7F-7L7.",
    "....F-J..F7FJ|L7L7L7",
    "....L7.F7||L7|.L7L7|",
    ".....|FJLJ|FJ|F7|.LJ",
    "....FJL-7.||.||||...",
    "....L---J.LJ.LJLJ...",
]


test_data_4 = [
    "FF7FSF7F7F7F7F7F---7",
    "L|LJ||||||||||||F--J",
    "FL-7LJLJ||||||LJL-77",
    "F--JF--7||LJLJ7F7FJ-",
    "L---JF-JLJ.||-FJLJJ7",
    "|F|F-JF---7F7-L7L|7|",
    "|FFJF7L7F-JF7|JL---7",
    "7-L-JL7||F7|L7F-7F7|",
    "L.L7LFJ|||||FJL7||LJ",
    "L7JLJL-JLJLJL--JLJ.L",
]


NODE_MAP = {
    "|": {"north": True, "south": True, "east": False, "west": False},
    "-": {"north": False, "south": False, "east": True, "west": True},
    "L": {"north": True, "south": False, "east": True, "west": False},
    "J": {"north": True, "south": False, "east": False, "west": True},
    "7": {"north": False, "south": True, "east": False, "west": True},
    "F": {"north": False, "south": True, "east": True, "west": False},
    ".": {"north": False, "south": False, "east": False, "west": False},
    "S": {"north": False, "south": False, "east": False, "west": False},
}


def get_puzzle_data(debug, test_data=None):
    if debug:
        data = test_data
    else:
        data = common.get_file_contents("../data/day10_input.txt")
    return data


class Node:
    def __init__(self, x, y, value, from_direction, to_direction):
        self.x = x
        self.y = y
        self.value = value
        self.from_direction = from_direction
        self.to_direction = to_direction
        self.steps = 0
        self.path_direction = None
        self.set_path_direction()

    def set_path_direction(self):
        if self.from_direction == "south" or self.to_direction == "north":
            self.path_direction = "up"
        elif self.from_direction == "north" or self.to_direction == "south":
            self.path_direction = "down"

    def get_node_key(self):
        return f"{self.x}-{self.y}"

    def __str__(self):
        return f"{self.x}, {self.y} - {self.value} - {self.from_direction}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y and self.value == other.value
        return False


def get_start_node(lines):
    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if char == "S":
                return Node(char_index, line_index, "S", None, None)

    return None


def get_first_node(node, map_data):
    directions = {"north": [-1, 0], "south": [1, 0], "east": [0, 1], "west": [0, -1]}

    direction_map = {"north": "south", "south": "north", "east": "west", "west": "east"}

    found = False

    for direction, pos_offset in directions.items():
        try:
            node_y = node.y + pos_offset[0]
            node_x = node.x + pos_offset[1]

            new_node = map_data[node_y][node_x]

            node_info = NODE_MAP[new_node]

            from_direction = direction_map[direction]

            if node_info[from_direction]:
                return Node(
                    node_x, node_y, new_node, direction_map[direction], direction
                )

        except IndexError:
            continue

    return None


def get_node_by_direction(row, col, direction, map_data):
    # print(row, col, direction)
    direction_map = {"north": "south", "south": "north", "east": "west", "west": "east"}

    from_direction = direction_map[direction]
    # print("from_direction", from_direction)

    try:
        if direction == "north":
            # return Node(col, row - 1, map_data[row - 1][col], from_direction, direction)
            # return {"node": map_data[row - 1][col], "pos": [row - 1, col]}
            # node_type = map_data[row-1][col]
            node_pos = (col, row - 1)
        elif direction == "east":
            # return Node(col + 1, row, map_data[row][col + 1], from_direction, direction)
            # return {"node": map_data[row][col + 1], "pos": [row, col + 1]}
            # node_type = map_data[row][col+1]
            node_pos = (col + 1, row)
        elif direction == "south":
            # return Node(col, row + 1, map_data[row + 1][col], from_direction, direction)
            # return {"node": map_data[row + 1][col], "pos": [row + 1, col]}
            # node_type = map_data[row+1][col]
            node_pos = (col, row + 1)
        elif direction == "west":
            # return Node(col - 1, row, map_data[row][col - 1], from_direction, direction)
            # return {"node": map_data[row][col - 1], "pos": [row, col - 1]}
            node_pos = (col - 1, row)
    except IndexError:
        return None

    node_type = map_data[node_pos[1]][node_pos[0]]
    # print("node_type", node_type)
    node_directions = dict(NODE_MAP[node_type])

    # print(node_directions.keys(), node_type)
    del node_directions[from_direction]

    for to_direction, is_valid in node_directions.items():
        if is_valid:
            # print("to_direction", to_direction)
            # print("------")
            return Node(
                node_pos[0], node_pos[1], node_type, from_direction, to_direction
            )

    return None


def get_next_node(current_node, prev_node, map_data):
    node_info = NODE_MAP[current_node.value]
    next_direction = None

    for direction, is_valid in node_info.items():
        if direction != current_node.from_direction and is_valid:
            next_direction = direction

    # print("Current node", current_node)
    # print("Prev node", prev_node)

    new_node = get_node_by_direction(
        current_node.y, current_node.x, next_direction, map_data
    )
    return new_node


def print_map(paths, map_data):
    map_list = []
    for row in map_data:
        map_list.append(list(row))

    for path in paths:
        map_list[path.y][path.x] = "*"

    for row in map_list:
        print("".join(row))


def part1(debug=True):
    lines = get_data(debug, test_data)
    start_node = get_start_node(lines)
    first_node = get_first_node(start_node, lines)

    path = [start_node, first_node]

    while True:
        next_node = get_next_node(path[-1], path[-2], lines)
        if next_node.value == "S":
            break
        path.append(next_node)

    steps = 0
    for p in path:
        p.steps = steps
        steps += 1

    steps = 1
    for p in reversed(path):
        # print(p.steps, p)
        if p.steps == steps:
            break
        p.steps = steps
        steps += 1

    max_steps = 0
    for p in path:
        if p.steps > max_steps:
            max_steps = p.steps

    print("Part 1: ", max_steps)


def is_point_in_shape_new(x, y, paths, max_width):
    # find first node to the right of our cur pos

    path_data = {}
    for path in paths:
        path_key = f"{path.x}-{path.y}"
        path_data[path_key] = path

    x += 1
    while True:
        test_key = f"{x}-{y}"
        if test_key in path_data.keys():
            return path_data[test_key].path_direction == "up"
        x += 1
        if x > max_width:
            break

    print("Found problem when testing", x, y)
    return False


def is_point_in_shape(x, y, paths):
    path_list = []

    for path in paths:
        path_list.append((path.x, path.y))

    num = len(path_list)
    j = num - 1
    result = False

    for i in range(num):
        if x == path_list[i][0] and y == path_list[i][1]:
            return True

        if (path_list[i][1] > y) != (path_list[j][1] > y):
            slope = (x - path_list[i][0]) * (path_list[j][1] - path_list[i][1]) - (
                path_list[j][0] - path_list[i][0]
            ) * (y - path_list[i][1])
            if slope == 0:
                return True

            if (slope < 0) != (path_list[j][1] < path_list[i][1]):
                result = not result
        j = i
    return result


def part2(debug=True):
    lines = get_data(debug, test_data_2)
    start_node = get_start_node(lines)
    first_node = get_first_node(start_node, lines)

    path = [start_node, first_node]

    while True:
        next_node = get_next_node(path[-1], path[-2], lines)
        if next_node.value == "S":
            break
        path.append(next_node)

    # for p in path:
    #     print(p)

    # print_map(path, lines)

    points = []

    for row_index, row in enumerate(lines):
        for col_index, col in enumerate(row):
            if col == ".":
                is_in_shape = is_point_in_shape(col_index, row_index, path)
                if is_in_shape:
                    points.append((col_index, row_index))

    print(len(points))


def pygame_test():
    import pygame
    from Engine.Engine import Engine
    from Engine import Config
    from Engine import DataManager

    class Game:  # 2
        def __init__(self):  # 3
            self.lines = lines
            self.all_nodes = []
            self.build_node_list()

            self.valid_direction = DataManager.get_data("valid_direction")

            self.start_node = get_start_node(self.lines)
            self.first_node = get_first_node(self.start_node, self.lines)

            self.all_nodes.remove(self.start_node.get_node_key())
            self.all_nodes.remove(self.first_node.get_node_key())

            self.path = [self.start_node, self.first_node]

            self.grid_size = grid_size

            self.width = self.grid_size * len(self.lines[0]) + (self.grid_size * 2)
            self.height = self.grid_size * len(self.lines) + (self.grid_size * 2)
            self.grid_surface = pygame.Surface(
                (self.width, self.height), pygame.SRCALPHA
            )

            self.cursor_pos = [0, 0]

            self.points = []

            self.line_index = 0
            self.char_index = 0

            self.directions = ["north", "south", "east", "west"]

            self.arrows = {}

            # i = 0

            while True:
                next_node = get_next_node(self.path[-1], self.path[-2], self.lines)

                if next_node is None or next_node.value == "S":
                    break
                self.path.append(next_node)
                self.all_nodes.remove(next_node.get_node_key())
                # i += 1

                # if i == 10:
                #     break

            self.generate_arrows()
            self.generate_points()
            self.render_grid()

            print("All Node Length:", len(self.all_nodes))

        def build_node_list(self):
            for y in range(len(self.lines)):
                for x in range(len(self.lines[0])):
                    node_key = f"{x}-{y}"
                    self.all_nodes.append(node_key)

        def is_point_in_shape(self, x, y, paths):
            path_list = []

            for path in paths:
                path_list.append((path.x, path.y))

            num = len(path_list)
            j = num - 1
            result = False

            for i in range(num):
                if x == path_list[i][0] and y == path_list[i][1]:
                    return True

                if (path_list[i][1] > y) != (path_list[j][1] > y):
                    slope = (x - path_list[i][0]) * (
                        path_list[j][1] - path_list[i][1]
                    ) - (path_list[j][0] - path_list[i][0]) * (y - path_list[i][1])
                    if slope == 0:
                        return True

                    if (slope < 0) != (path_list[j][1] < path_list[i][1]):
                        result = not result
                j = i
            return result

        def is_point_in_shape_new(self, x, y, paths):
            # find first node to the right of our cur pos

            max_width = len(self.lines[0])

            path_data = {}
            for path in paths:
                path_key = f"{path.x}-{path.y}"
                path_data[path_key] = path

            x += 1
            while True:
                test_key = f"{x}-{y}"
                if test_key in path_data.keys():
                    return path_data[test_key].path_direction == self.valid_direction
                x += 1
                if x > max_width:
                    break

            return False

        def generate_points(self):
            for row_index, row in enumerate(self.lines):
                for col_index, col in enumerate(row):
                    if col == ".":
                        # is_in_shape = self.is_point_in_shape(
                        #     col_index, row_index, self.path
                        # )
                        is_in_shape = self.is_point_in_shape_new(
                            col_index, row_index, self.path
                        )
                        node_key = f"{col_index}-{row_index}"
                        self.all_nodes.remove(node_key)

                        if is_in_shape:
                            self.points.append((col_index, row_index))

            for other_point in self.all_nodes:
                x, y = other_point.split("-")
                x = int(x)
                y = int(y)
                is_in_shape = self.is_point_in_shape_new(x, y, self.path)
                if is_in_shape:
                    self.points.append((x, y))

            print("Path Points: ", len(self.points))

        def update(self, dt):  # 4
            pass

        def generate_arrows(self):
            arrow_types = list(itertools.permutations(self.directions, r=2))
            half_size = self.grid_size // 2
            quarter_size = half_size // 2

            center = (half_size, half_size)

            for arrow_type in arrow_types:
                start, end = arrow_type

                surface = pygame.Surface(
                    (self.grid_size, self.grid_size), pygame.SRCALPHA
                )

                if start == "north":
                    pygame.draw.line(surface, (0, 0, 0), (half_size, 0), center)

                elif start == "south":
                    pygame.draw.line(
                        surface, (0, 0, 0), (half_size, self.grid_size), center
                    )

                elif start == "east":
                    pygame.draw.line(
                        surface, (0, 0, 0), (self.grid_size, half_size), center
                    )

                elif start == "west":
                    pygame.draw.line(surface, (0, 0, 0), (0, half_size), center)

                if end == "north":
                    pygame.draw.line(surface, (0, 0, 0), center, (half_size, 0))
                    pygame.draw.line(
                        surface, (0, 0, 0), (quarter_size, quarter_size), (half_size, 0)
                    )
                    pygame.draw.line(
                        surface,
                        (0, 0, 0),
                        (half_size + quarter_size, quarter_size),
                        (half_size, 0),
                    )

                elif end == "south":
                    pygame.draw.line(
                        surface, (0, 0, 0), center, (half_size, self.grid_size)
                    )
                    pygame.draw.line(
                        surface,
                        (0, 0, 0),
                        (quarter_size, half_size + quarter_size),
                        (half_size, self.grid_size),
                    )
                    pygame.draw.line(
                        surface,
                        (0, 0, 0),
                        (half_size + quarter_size, half_size + quarter_size),
                        (half_size, self.grid_size),
                    )

                elif end == "east":
                    pygame.draw.line(
                        surface, (0, 0, 0), center, (self.grid_size, half_size)
                    )
                    pygame.draw.line(
                        surface,
                        (0, 0, 0),
                        (half_size + quarter_size, quarter_size),
                        (self.grid_size, half_size),
                    )
                    pygame.draw.line(
                        surface,
                        (0, 0, 0),
                        (half_size + quarter_size, half_size + quarter_size),
                        (self.grid_size, half_size),
                    )

                elif end == "west":
                    pygame.draw.line(surface, (0, 0, 0), center, (0, half_size))
                    pygame.draw.line(
                        surface, (0, 0, 0), (quarter_size, quarter_size), (0, half_size)
                    )
                    pygame.draw.line(
                        surface,
                        (0, 0, 0),
                        (quarter_size, half_size + quarter_size),
                        (0, half_size),
                    )

                self.arrows[f"{start}-{end}"] = surface

        def draw_arrow(self, width, height, from_direction, to_direction=None):
            arrow_key = f"{from_direction}-{to_direction}"
            surface = pygame.Surface((width, height), pygame.SRCALPHA)

            if arrow_key in self.arrows.keys():
                return self.arrows[arrow_key]
            else:
                print(f"Unable to find {arrow_key}")

            return surface

        def render_grid(self):
            for line_index, line in enumerate(self.lines):
                for char_index, char in enumerate(line):
                    color = (200, 0, 0)
                    if char == ".":
                        color = (0, 100, 0)
                    elif char == "S":
                        color = (255, 255, 255)
                    pygame.draw.rect(
                        self.grid_surface,
                        color,
                        (
                            char_index * self.grid_size,
                            line_index * self.grid_size,
                            self.grid_size,
                            self.grid_size,
                        ),
                    )

            prev_path = None
            for path in self.path:
                if path.value == "S":
                    continue
                arrow = self.draw_arrow(
                    self.grid_size,
                    self.grid_size,
                    path.from_direction,
                    path.to_direction,
                )
                self.grid_surface.blit(
                    arrow, (path.x * self.grid_size, path.y * self.grid_size)
                )

            for point in self.points:
                pygame.draw.rect(
                    self.grid_surface,
                    (0, 0, 200),
                    (
                        point[0] * self.grid_size,
                        point[1] * self.grid_size,
                        self.grid_size,
                        self.grid_size,
                    ),
                )

            pygame.draw.rect(
                self.grid_surface,
                (0, 255, 255),
                (
                    self.cursor_pos[0] * self.grid_size,
                    self.cursor_pos[1] * self.grid_size,
                    self.grid_size,
                    self.grid_size,
                ),
            )

            # for point in self.all_nodes:
            #     x, y = point.split("-")
            #     x = int(x)
            #     y = int(y)

            #     pygame.draw.rect(
            #         self.grid_surface,
            #         (0, 255, 0),
            #         (
            #             x * self.grid_size,
            #             y * self.grid_size,
            #             self.grid_size,
            #             self.grid_size,
            #         ),
            #     )

            if DataManager.get_data("create_screenshot"):
                pygame.image.save(self.grid_surface, "grid.png")

        def draw(self, canvas):  # 5
            canvas.blit(self.grid_surface, (0, 0))

        def get_tile_at_pos(self, x, y):
            return self.lines[y][x]

        def handle_event(self, event):  # 6
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    # up
                    if self.cursor_pos[1] == 0:
                        return

                    self.cursor_pos[1] -= 1
                elif event.key == pygame.K_s:
                    # down
                    if self.cursor_pos[1] == len(self.lines):
                        return

                    self.cursor_pos[1] += 1
                elif event.key == pygame.K_a:
                    # left
                    if self.cursor_pos[0] == 0:
                        return

                    self.cursor_pos[0] -= 1
                elif event.key == pygame.K_d:
                    # right
                    if self.cursor_pos[0] == len(self.lines[0]):
                        return

                    self.cursor_pos[0] += 1
                elif event.key == pygame.K_SPACE:
                    tile = self.get_tile_at_pos(self.cursor_pos[0], self.cursor_pos[1])
                    print(tile)

    debug = False
    lines = get_puzzle_data(debug, test_data_4)
    grid_size = 8

    y_size = len(lines) * grid_size + (grid_size * 2)
    x_size = len(lines[0]) * grid_size + (grid_size * 2)

    Config.set_screensize(x_size, y_size)

    DataManager.set_data("create_screenshot", True)
    DataManager.set_data("valid_direction", "up")

    e = Engine(Game)  # 7
    e.game_loop()  # 8


if __name__ == "__main__":
    # part1(False) # 6828
    # part2(False) # 459
    pygame_test()
