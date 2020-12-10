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


def find_missing_seat(seat_list):
    for i in range(8):
        if i not in seat_list:
            print(i)
            return i
    return False


def part2():
    seats = {}
    for line in data:
        row = find_row(line)
        col = find_seat(line)
        seat_id = get_seat_id(row, col)
        if row not in seats.keys():
            seats[row] = []
        seats[row].append(col)
    
    sorted_keys = sorted(seats.keys())

    missing_seat = None
    found_row = None
    for index, k in enumerate(sorted_keys):
        if index == 0 or index == sorted_keys[-1] or len(seats[k]) == 1:
            continue
        if len(seats[k]) != 8:
            missing_seat = find_missing_seat(seats[k])
            found_row = k
            break

    return get_seat_id(k, missing_seat)
    



def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
