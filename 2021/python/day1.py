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

	return inc_count


def p2():
	# the last iterations total
	current = None

	# our result
	inc_count = 0

	lines = get_file_contents("data/day1_input.txt")
	line_count = len(lines)

	# here we loop over the list of numbers
	# on each loop, we need to total the current line along with the next 2 items
	# and see if that is bigger than our last check
	for index, line in enumerate(lines):
		# if current is None, this is our first time through, and we just need to set current
		if current is None:
			current = int(line) + int(lines[index + 1]) + int(lines[index + 2])
		else:
			# otherwise we need to be sure we have 2 more items to check for our total of 3
			if index < (line_count - 2):
				# if so, count our total and do our check
				total = int(line) + int(lines[index + 1]) + int(lines[index + 2])
				if total > current:
					inc_count += 1
				current = total

	return inc_count

if __name__ == '__main__':
	print("Part 1: ", p1())
	print("Part 2: ", p2())
