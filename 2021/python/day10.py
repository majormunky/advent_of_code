from common import get_file_contents


openers = ["{", "[", "<", "("]
closers = ["}", "]", ">", ")"]


def check_line(line):
	line_data = []
	for c in line:
		if c in openers:
			# print("found opener", c)
			line_data.append(c)
		else:
			# this character is a closing bracket
			# we need to check if the last item in our line data list is the matching opener
			# for this particular closer

			# get the index of the current character
			closer_index = closers.index(c)

			# this is the opener character for the current closing bracket
			opener_char = openers[closer_index]

			# check if the last item in our list is the matching opening statement
			if opener_char == line_data[-1]:
				# print("found closer", c, "matching opener", opener_char)
				# if so, we can remove the item in our list
				line_data.pop()
			else:
				# print("last opener", line_data[-1], "didn't match", opener_char)
				#  if not, then this is an invalid string
				return "corrupt", c

	if len(line_data):
		# print("line incomplete, we have", len(line_data), "items left")
		# print(line_data)
		return "incomplete", None
	return "normal", None


def get_data():
	source = "real"

	test_data = """
		[({(<(())[]>[[{[]{<()<>>
		[(()[<>])]({[<{<<[]>>(
		{([(<{}[<>[]}>{[]{[(<()>
		(((({<>}<{<{<>}{[]{[]{}
		[[<[([]))<([[{}[[()]]]
		[{[{({}]{}}([{[{{{}}([]
		{<[[]]>}<{[{[{[]{()[[[]
		[<(<(<(<{}))><([]([]()
		<{([([[(<>()){}]>(<<{{
		<{([{{}}[<[[[<>{}]]]>[]]
	"""

	if source == "real":
		return get_file_contents("data/day10_input.txt")
	else:
		result = []
		for line in test_data.split("\n"):
			if line:
				result.append(line.strip())
		return result


def p1():
	lines = get_data()
	result = {
		"corrupt": [],
		"incomplete": [],
		"normal": [],
	}

	for line_index, line in enumerate(lines):
		line_result = check_line(line)
		# print("----------------", line_index, line_result)
		if line_result[0] == "corrupt":
			result[line_result[0]].append([line, line_result[1]])
		else:	
			result[line_result[0]].append(line)

	# print("Corrupt:", len(result["corrupt"]))
	# print("Incomplete:", len(result["incomplete"]))
	# print("Normal:", len(result["normal"]))
	# print(result["corrupt"])

	points = {
		"}": 1197,
		")": 3,
		"]": 57,
		">": 25137
	}

	score = 0
	for corrupt_item in result["corrupt"]:
		score += points[corrupt_item[1]]
	return score
def p2():
	pass


if __name__ == '__main__':
	print("Part 1:", p1())
	print("Part 2:", p2())
