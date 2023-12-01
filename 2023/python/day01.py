import os
import string
import common


test_data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]


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


if __name__ == "__main__":
    part1()  # 54697
