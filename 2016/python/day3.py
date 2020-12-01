import common


data = common.get_file_contents("data/day3_input.txt")


def get_parts(data):
    result = []
    for part in data.split(" "):
        if len(part) > 0:
            result.append(part)
    return result


def is_real_triangle(data):
    parts = get_parts(data)
    side1 = int(parts[0])
    side2 = int(parts[1])
    side3 = int(parts[2])

    if side1 + side2 > side3 and side1 + side3 > side2 and side3 + side2 > side1:
        return True
    return False


def part1():
    real_triangles = 0
    for line in data:
        if is_real_triangle(line):
            real_triangles += 1
    return real_triangles


def part2():
    return "not complete"


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
