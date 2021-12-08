from common import get_file_contents


def p1():
	lines = get_file_contents("data/day8_input.txt")
	# the digits dict represents a mapping between how many segments are active
	# and the actual value that is supposed to be reprenenting
	digits = {
		2: 1,
		3: 7,
		4: 4,
		7: 8
	}
	found = 0

	for line in lines:
		parts = line.split("|")
		more_parts = parts[1].split(" ")
		for item in more_parts:
			if len(item) in digits.keys():
				found += 1
	return found


def p2():
	pass


if __name__ == '__main__':
	print("Part 1:", p1())
	print("Part 2:", p2())
