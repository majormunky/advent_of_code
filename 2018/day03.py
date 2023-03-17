from common import get_file_contents


def parse_line(line):
    parts = line.split(" ")
    return {
        "number": parts[0].replace("#", ""),
        "left": int(parts[2].split(",")[0]),
        "top": int(parts[2].split(",")[1].replace(":", "")),
        "width": int(parts[3].split("x")[0]),
        "height": int(parts[3].split("x")[1]),
    }


def print_grid(grid):
    for line in grid:
        print(line)


def generate_grid(width, height):
    return [["." for x in range(width)] for y in range(height)]


def update_grid(data, grid):
    for x in range(data["left"], data["left"] + data["width"]):
        for y in range(data["top"], data["top"] + data["height"]):
            if grid[y][x] == ".":
                grid[y][x] = data["number"]
            elif grid[y][x] == "X":
                continue
            else:
                grid[y][x] = "X"
    return grid


def count_cells(grid):
    count = 0
    for x in grid:
        for y in x:
            if y == "X":
                count += 1
    return count


def check_grid(lines, grid):
    current_num = None
    for line in lines:
        data = parse_line(line)
        current_num = data["number"]
        so_far_so_good = True
        for x in range(data["left"], data["left"] + data["width"]):
            for y in range(data["top"], data["top"] + data["height"]):
                if grid[y][x] != data["number"]:
                    so_far_so_good = False
        if so_far_so_good:
            return current_num


def part1():
    # lines = [
    #     "#1 @ 1,3: 4x4",
    #     "#2 @ 3,1: 4x4",
    #     "#3 @ 5,5: 2x2"
    # ]
    lines = get_file_contents("data/day03-input.txt")

    grid = generate_grid(1000, 1000)

    for i in lines:
        data = parse_line(i)
        grid = update_grid(data, grid)

    answer = count_cells(grid)
    return answer


def part2():
    # lines = [
    #     "#1 @ 1,3: 4x4",
    #     "#2 @ 3,1: 4x4",
    #     "#3 @ 5,5: 2x2"
    # ]
    lines = get_file_contents("data/day03-input.txt")
    grid = generate_grid(1000, 1000)
    for i in lines:
        data = parse_line(i)
        grid = update_grid(data, grid)

    answer = check_grid(lines, grid)
    return answer


def main():
    answer1 = part1()
    answer2 = part2()
    print("Part 1: ", answer1)
    print("Part 2: ", answer2)

if __name__ == "__main__":
    main()
