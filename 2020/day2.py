import sys
import common


def get_filename():
    filename = sys.argv[0]
    filename = filename.split("/")[-1]
    filename = filename.split(".")[0]
    return filename

data = common.get_file_contents("data/{}_input.txt".format(get_filename()))


def check_password(line):
    # break our line up into parts ['1-3', 'a:', 'abc123']
    parts = line.split(" ")

    # fix the check letter so we dont have the colon
    check_letter = parts[1].replace(":", "")

    # break up our 1-3 into separate numbers
    amount_min, amount_max = parts[0].split("-")

    # do our count on how many times our check letter shows up
    letter_amount = parts[2].count(check_letter)

    # our letter amount should sit between the min and max to be valid
    if int(amount_min) <= letter_amount <= int(amount_max):
        return True
    return False


def part1():
    result = 0
    for item in data:
        if check_password(item):
            result += 1
    return result


def part2():
    return "not complete"


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()

