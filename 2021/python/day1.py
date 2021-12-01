from common import get_file_contents


def p1():
	lines = get_file_contents("data/day1_input.txt")
	current = None
	inc_count = 0

	for line in lines:
		if current is None:
			current = int(line)
		else:
			if int(line) > current:
				inc_count += 1
			current = int(line)

	print(inc_count)


if __name__ == '__main__':
	p1()