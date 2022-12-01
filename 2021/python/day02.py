from common import get_file_contents


def p1():
	lines = get_file_contents("data/day2_input.txt")
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
	lines = get_file_contents("data/day2_input.txt")
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
	# 2150351
	print("Part 1: ", p1())

	# 1842742223
	print("Part 2: ", p2())
