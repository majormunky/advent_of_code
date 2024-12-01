import os
import common


# def get_filename():
#     filename = sys.argv[0]
#     filename = filename.split("/")[-1]
#     filename = filename.split(".")[0]
#     return filename

# data = common.get_file_contents("data/{}_input.txt".format(get_filename()), single_line=True)



def part1():
    real_file = os.path.join("..", "data", "day01_input.txt")
    data = common.get_file_contents(real_file, single_line=True)

    answer = 0
    for index, character in enumerate(data):
        try:
            next_char = data[index + 1]
            if next_char == character:
                answer += int(character)
        except IndexError:
            pass
    if data[0] == data[-1]:
        answer += int(data[0])
    return answer


def part2():
    real_file = os.path.join("..", "data", "day01_input.txt")
    data = common.get_file_contents(real_file, single_line=True)

    answer = 0
    # figure out what half of our list size is
    half_len = len(data) / 2
    for index, character in enumerate(data):
        try:
            # use mod to make sure we don't overflow our list
            next_index = int((half_len + index) % len(data))
            next_char = data[next_index]
            if next_char == character:
                answer += int(character)
        except IndexError:
            pass
    return answer


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
