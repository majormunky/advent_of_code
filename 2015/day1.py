import common


def main():
	part2()


def part2():
	data = common.get_file_contents("data/day1_input.txt")[0]
	floor = 0
	for index, char in enumerate(data):
		if char == ")":
			floor -= 1
		elif char == "(":
			floor += 1
		if floor < 0:
			print(index + 1)
			break



def part1():
	data = common.get_file_contents("data/day1_input.txt")[0]
	
	floor = 0
	for char in data:
		if char == ")":
			floor -= 1
		elif char == "(":
			floor += 1
	print(floor)


if __name__ == '__main__':
	main()
