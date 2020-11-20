import common


def main():
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
