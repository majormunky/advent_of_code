import common
import string

test_lines = ["Sabqponm", "abcryxxl", "accszExk", "acctuvwj", "abdefghi"]


# test_map = [
#     ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
#     ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
#     ["#", ".", ".", ".", ".", ".", ".", ".", "E", ".", "#"],
#     ["#", "#", "#", "#", "#", "#", "#", "#", ".", ".", "#"],
#     ["#", ".", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
#     ["#", ".", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
#     ["#", ".", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
#     ["#", ".", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
#     ["#", ".", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
#     ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
#     ["#", ".", "S", ".", ".", ".", ".", ".", ".", ".", "#"],
#     ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
#     ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
#     ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
# ]


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_next_node(distance_data, node_data):
    best = None
    best_value = 1_000_000_000

    for index, node in enumerate(node_data):
        node_key = build_pos_key(node)
        node_score = distance_data[node_key]
        if node_score < best_value:
            best = index
            best_value = node_score

    return node_data[best]


def build_pos_key(pos):
    return f"{pos[0]}-{pos[1]}"


def find_neighbors(pos, map):
    x, y = pos
    
    # up
    if y >= 1:
        yield (x, y - 1)

    # down
    if y < len(map) - 1:
        yield (x, y + 1)

    # left
    if x >= 1:
        yield (x - 1, y)

    # right
    if (x < len(map[0]) - 1):
        yield (x + 1, y)


def reconstruct_path(came_from_dict, current):
    result = [current]
    current_key = build_pos_key(current)

    while True:
        if current_key not in came_from_dict.keys():
            break
        current = came_from_dict[current_key]
        current_key = build_pos_key(current)
        result.insert(0, current)

    return result


def find_a_star_path(start, end, map_data):
    elevation_data = build_elevation_data()

    start_key = build_pos_key(start)

    open_set = [start]
    came_from = {}

    g_score = {}
    g_score[start_key] = 0

    f_score = {}
    f_score[start_key] = manhattan_distance(start, end)

    while len(open_set):
        # returns it as a string
        current = get_next_node(f_score, open_set)

        current_key = build_pos_key(current)
        current_val = map_data[current[1]][current[0]]

        # print(current, current_val)

        # check if we are done
        if list(current) == end:
            return reconstruct_path(came_from, current)

        # remove the current node from our nodes to check
        open_set.remove(current)

        current_elevation = elevation_data[current_val]
        # print("current elevation", current_elevation)

        # check each neighbor
        for neighbor in find_neighbors(current, map_data):
            # print(" ", neighbor)
            neighbor_key = build_pos_key(neighbor)
            neighbor_value = map_data[neighbor[1]][neighbor[0]]
            if neighbor_value == "S":
                continue
            # print("  neighbor val", neighbor_value)
            neighbor_elevation = elevation_data[neighbor_value]
            # elevation_diff = current_elevation - neighbor_elevation
            g_score_increase = 1
            # print(f"  neighbor elevation - {neighbor_elevation}")
            # print(f"  elevation diff - {elevation_diff}")
            # 
            if neighbor_elevation > current_elevation + 1:
                g_score_increase = 1_000_000_000

            node_g_score = g_score[current_key] + g_score_increase
            if node_g_score < g_score.get(neighbor_key, 1_000_000_000):
                came_from[neighbor_key] = current
                g_score[neighbor_key] = node_g_score
                f_score[neighbor_key] = node_g_score + manhattan_distance(neighbor, end)
                if neighbor not in open_set:
                    open_set.append(neighbor)

    return False


def output_result(node_path, map_data):
    for node in node_path:
        x, y = node
        map_data[y][x] = "@"


    for row in map_data:
        output = "".join(row)
        print(output)


def build_elevation_data():
    result = {}

    for index, char in enumerate(string.ascii_lowercase):
        result[char] = index

    result["S"] = 0
    result["E"] = 25

    return result


def get_data(debug, test_data):
    if debug:
        data = test_data
    else:
        data = common.get_file_contents("data/day12_input.txt")
    return data


def get_pos(lines, char):
    for line_index, line in enumerate(lines):
        if char in line:
            return [line.index(char), line_index]


def get_neighbors(lines, pos):
    result = {"^": None, "v": None, "<": None, ">": None}
    x, y = pos

    if y > 0:
        result["^"] = {"pos": [x, y - 1], "value": lines[y - 1][x]}

    if y < len(lines) - 1:
        result["v"] = {"pos": [x, y + 1], "value": lines[y + 1][x]}

    if x > 0:
        result["<"] = {"pos": [x - 1, y], "value": lines[y][x - 1]}

    if x < len(lines[0]) - 1:
        result[">"] = {"pos": [x + 1, y], "value": lines[y][x + 1]}

    return result


def find_path(current_path, lines):
    x, y = current_path[-1]
    current_node = lines[y][x]

    if current_node == "E":
        yield current_path
    else:
        current_elevation = elevation_data[current_node]
        neighbors = get_neighbors(lines, (x, y))
        for direction, neighbor in neighbors.items():
            if neighbor and neighbor["pos"] not in current_path:
                neighbor_height = elevation_data[neighbor["value"]]
                elevation_diff = current_elevation - neighbor_height
                if elevation_diff > -2:
                    # print(current_node, neighbor["value"], elevation_diff)
                    for result in find_path(current_path + [neighbor["pos"]], lines):
                        yield result


def output_path(steps, lines):
    width = len(lines[0])
    height = len(lines)
    total_steps = len(steps)
    print("total steps:", total_steps)

    output = []

    for row in range(height):
        output.append([])
        for col in range(width):
            output[row].append(".")

    for pos_index, pos in enumerate(steps):
        x, y = pos

        direction = None

        if pos_index < (total_steps - 1):
            next_pos = steps[pos_index + 1]
            if next_pos[0] == (pos[0] - 1):
                direction = "<"
            elif next_pos[0] == (pos[0] + 1):
                direction = ">"
            elif next_pos[1] == (pos[1] - 1):
                direction = "^"
            else:
                direction = "v"

        if direction is None:
            output[y][x] = "."
        else:
            output[y][x] = direction

    for row in output:
        print("".join(row))


def part2(debug=True):
    lines = get_data(debug, test_lines)


def part1(debug=True):
    lines = get_data(debug, test_lines)
    start_pos = get_pos(lines, "S")
    end_pos = get_pos(lines, "E")

    results = find_a_star_path(start_pos, end_pos, lines)
    if results:
        print(len(results) - 1)


if __name__ == "__main__":
    part1(False) #380
    part2()
