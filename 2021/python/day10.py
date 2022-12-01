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
        return "incomplete", line_data
    return "normal", None


def get_data(source="real"):
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


def organize_data(lines):
    result = {
        "corrupt": [],
        "incomplete": [],
        "normal": [],
    }

    for line_index, line in enumerate(lines):
        line_result = check_line(line)
        # print("----------------", line_index, line_result)
        if line_result[0] in ["corrupt", "incomplete"]:
            result[line_result[0]].append([line, line_result[1]])
        else:
            result[line_result[0]].append(line)
    return result


def p1():
    lines = get_data()
    result = organize_data(lines)

    points = {"}": 1197, ")": 3, "]": 57, ">": 25137}

    score = 0
    for corrupt_item in result["corrupt"]:
        score += points[corrupt_item[1]]
    return score


def fix_line(line_items):
    result = []
    for item in line_items:
        opener_index = openers.index(item)
        closer_char = closers[opener_index]
        result.append(closer_char)
    result.reverse()
    return result


def score_item(char_list):
    points = {")": 1, "]": 2, "}": 3, ">": 4}

    score = 0

    for item in char_list:
        score *= 5
        item_point = points[item]
        score += item_point
    return score


def p2():
    lines = get_data("real")
    result = organize_data(lines)

    score_list = []

    for item in result["incomplete"]:
        fix = fix_line(item[1])
        score = score_item(fix)
        score_list.append(score)
    score_list = sorted(score_list)
    len_scores = len(score_list)
    middle_index = len_scores // 2
    return score_list[middle_index]


if __name__ == "__main__":
    print("Part 1:", p1())
    print("Part 2:", p2())
