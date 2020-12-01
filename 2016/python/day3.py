import common


data = common.get_file_contents("data/day3_input.txt")


def get_parts(data):
    result = []
    for part in data.split(" "):
        if len(part) > 0:
            result.append(part)
    return result


def is_real_triangle(data, as_tuple=False):
    if as_tuple:
        side1 = int(data[0])
        side2 = int(data[1])
        side3 = int(data[2])
    else:
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


def check_columns(data):
    line1 = get_parts(data[0])
    line2 = get_parts(data[1])
    line3 = get_parts(data[2])

    triangles = []
    triangles.append((line1[0], line2[0], line3[0]))
    triangles.append((line1[1], line2[1], line3[1]))
    triangles.append((line1[2], line2[2], line3[2]))

    answer = 0
    for t in triangles:
        if is_real_triangle(t, as_tuple=True):
            answer += 1
    return answer


def part2():
    to_check = []
    answer = 0

    test_data = [
        "101 301 501",
        "102 302 502",
        "103 303 503",
        "201 401 601",
        "202 402 602",
        "203 403 603",
    ]

    for line in data:
        to_check.append(line)
        if len(to_check) == 3:
            answer += check_columns(to_check)
            to_check = []
    return answer


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
