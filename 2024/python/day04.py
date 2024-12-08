import os
import common


def part01():
    # test_path = os.path.join("..", "data", "day04_sample.txt")
    real_path = os.path.join("..", "data", "day04_input.txt")
    lines = common.get_file_contents(real_path)

    width = len(lines[0])
    height = len(lines)

    answer = 0

    for y in range(height):
        for x in range(width):
            char = lines[y][x]
            if char == "X":
                # check for M surrounding this letter
                # up
                if y > 2 and lines[y-1][x] == "M" and lines[y-2][x] == "A" and lines[y-3][x] == "S":
                    answer += 1
                # right
                if x < width - 3 and lines[y][x+1] == "M" and lines[y][x+2] == "A" and lines[y][x+3] == "S":
                    answer += 1
                # down
                if y < height - 3 and lines[y+1][x] == "M" and lines[y+2][x] == "A" and lines[y+3][x] == "S":
                    answer += 1
                # left
                if x > 2 and lines[y][x-1] == "M" and lines[y][x-2] == "A" and lines[y][x-3] == "S":
                    answer += 1
                # top right
                if y > 2 and x < width - 3 and lines[y-1][x+1] == "M" and lines[y-2][x+2] == "A" and lines[y-3][x+3] == "S":
                    answer += 1
                # bottom right
                if y < height - 3 and x < width - 3 and lines[y+1][x+1] == "M" and lines[y+2][x+2] == "A" and lines[y+3][x+3] == "S":
                    answer += 1
                # bottom left
                if y < height - 3 and x > 2 and lines[y+1][x-1] == "M" and lines[y+2][x-2] == "A" and lines[y+3][x-3] == "S":
                    answer += 1
                # top left
                if y > 2 and x > 2 and lines[y-1][x-1] == "M" and lines[y-2][x-2] == "A" and lines[y-3][x-3] == "S":
                    answer += 1
    return answer



def part02():
    # test_path = os.path.join("..", "data", "day04_sample.txt")
    real_path = os.path.join("..", "data", "day04_input.txt")
    lines = common.get_file_contents(real_path)

    width = len(lines[0])
    height = len(lines)

    answer = 0

    for y in range(height):
        for x in range(width):
            char = lines[y][x]

            if char != "M" and char != "S":
                continue

            # check if we are at the edge of the board
            if y > height - 3 or x > width - 3:
                continue

            # does the 2nd letter after this match an S or M?
            if lines[y][x+2] not in ["S", "M"]:
                continue

            # does the center of the X match an A
            if lines[y+1][x+1] != "A":
                continue

            # do a full check now
            # top left of X is an M and top right of X is an M
            if char == "M" and lines[y][x+2] == "M" and lines[y+2][x+2] == "S" and lines[y+2][x] == "S":
                answer += 1
                continue

            # top left of X is an M and top right of X is an S
            if char == "M" and lines[y][x+2] == "S" and lines[y+2][x+2] == "S" and lines[y+2][x] == "M":
                answer += 1
                continue

            # top left of X is an S and top right of X is an M
            if char == "S" and lines[y][x+2] == "M" and lines[y+2][x+2] == "M" and lines[y+2][x] == "S":
                answer += 1
                continue

            # top left of X is an S and top right of X is an S
            if char == "S" and lines[y][x+2] == "S" and lines[y+2][x+2] == "M" and lines[y+2][x] == "M":
                answer += 1
                continue

    return answer


if __name__ == "__main__":
    part1_answer = part01()
    part2_answer = part02()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")
