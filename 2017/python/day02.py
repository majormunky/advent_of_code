import os
import common


def get_parts(line):
    result = []
    for item in line.split(" "):
        if len(item) > 0:
            result.append(int(item))
    return result


def part1():
    real_file = os.path.join("..", "data", "day02_input.txt")
    data = common.get_file_contents(real_file)

    answer = 0
    for line in data:
        line_parts = get_parts(line)
        min_num = min(*line_parts)
        max_num = max(*line_parts)
        diff = max_num - min_num
        answer += diff
    return answer


def part2():
    real_file = os.path.join("..", "data", "day02_input.txt")
    data = common.get_file_contents(real_file)

    answer = 0

    for line in data:
        line_answer = 0
        line_parts = get_parts(line)

        for i in line_parts:
            for j in line_parts:
                if i == j:
                    continue
                if int(i) % int(j) == 0:
                    line_answer = int(int(i) / int(j))
        answer += line_answer
    return answer


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
