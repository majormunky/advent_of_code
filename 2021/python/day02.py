import os
import common


def p1():
    real_file = os.path.join("..", "data", "day02_input.txt")
    lines = common.get_file_contents(real_file)

    x = 0
    y = 0

    for line in lines:
        command, amount = line.split(" ")
        if command == "forward":
            x += int(amount)
        elif command == "down":
            y += int(amount)
        elif command == "up":
            y -= int(amount)
    return x * y


def p2():
    real_file = os.path.join("..", "data", "day02_input.txt")
    lines = common.get_file_contents(real_file)

    x = 0
    y = 0
    aim = 0

    for line in lines:
        command, amount = line.split(" ")
        if command == "forward":
            x += int(amount)
            y += aim * int(amount)
        elif command == "down":
            aim += int(amount)
        elif command == "up":
            aim -= int(amount)
    return x * y

if __name__ == '__main__':
	print("Part 1: ", p1())
	print("Part 2: ", p2())
