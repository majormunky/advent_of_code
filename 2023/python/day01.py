import os
import string
import common


test_data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]


def check_for_string_numbers(line):
    # holds our string of numbers found in the line
    result = ""

    # lookup table for string to num values
    num_strings = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    num_keys = num_strings.keys()

    # where are we at in the string
    current_char = 0
    str_length = len(line)

    # here we are going character by character within the string
    # this needs to be done this way in cases where we have two
    # num strings that re-use a character, like threeight
    while True:
        if line[current_char] not in string.ascii_letters:
            # this is a number
            result += line[current_char]
        else:
            # this is a letter
            # go over each of our num strings
            for num_item in num_keys:
                # to see if our sub-string starts with a num word
                if line[current_char:].startswith(num_item):
                    result += num_strings[num_item]

        # increment our current position within the line
        current_char += 1

        # check to see if we need to break out of our loop
        if current_char >= str_length:
            break

    return int(result[0] + result[-1])


def part1():
    # store final answer
    result = 0

    filepath = os.path.join("data", "day01_input.txt")

    # get lines
    lines = common.get_file_contents(filepath)

    for line in lines:
        # build up numbers in this line
        line_answer = ""

        # go over each character
        for char in line:
            # check to see if this is a number
            if char not in string.ascii_letters:
                # if so, append it to our string of numbers
                line_answer += char

        # we now have our final string, but we just need the first
        # and last characters for the number to add
        line_answer = line_answer[0] + line_answer[-1]

        # increment our result with the line amount
        result += int(line_answer)
    print(result)


def part2():
    # store final answer
    result = 0

    filepath = os.path.join("data", "day01_input.txt")

    # get lines
    lines = common.get_file_contents(filepath)

    for line in lines:
        line_result = check_for_string_numbers(line)
        result += line_result

    print(result)


if __name__ == "__main__":
    part1()  # 54697
    part2()  # 54885
