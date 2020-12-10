import sys
import common


def get_filename():
    filename = sys.argv[0]
    filename = filename.split("/")[-1]
    filename = filename.split(".")[0]
    return filename


data = common.get_file_contents("data/{}_input.txt".format(get_filename()))


def find_row(line):
    bits = [0, 0, 0, 0, 0, 0, 0, 0]
    answer = 0
    if line[0] == "B":
        answer += 64
    if line[1] == "B":
        answer += 32
    if line[2] == "B":
        answer += 16
    if line[3] == "B":
        answer += 8
    if line[4] == "B":
        answer += 4
    if line[5] == "B":
        answer += 2
    if line[6] == "B":
        answer += 1
    return answer


def find_seat(line):
    answer = 0
    if line[7] == "R":
        answer += 4
    if line[8] == "R":  
        answer += 2
    if line[9] == "R":
        answer += 1
    return answer


def get_seat_id(row, col):
    return  row * 8 + col


def part1():
    highest = 0
    for line in data:
        row = find_row(line)
        col = find_seat(line)
        seat_id = get_seat_id(row, col)
        if seat_id > highest:
            highest = seat_id
    return highest

def part2():
    return None


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
