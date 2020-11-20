import common


data = common.get_file_contents("data/day5_input.txt")


def check_for_two_characters_together(string):
	last_char = None
	for char in string:
		if last_char is None:
			last_char = char
			continue

		if char == last_char:
			return True

		last_char = char

	return False



def check_if_nice(string):
	vowel_count = 0
	vowel_count += string.count("a")
	vowel_count += string.count("e")
	vowel_count += string.count("i")
	vowel_count += string.count("o")
	vowel_count += string.count("u")

	if vowel_count <= 2:
		return False

	if "ab" in string:
		return False

	if "cd" in string:
		return False

	if "pq" in string:
		return False

	if "xy" in string:
		return False

	return check_for_two_characters_together(string)
	

def test():
	test_inputs = {
		"ugknbfddgicrmopn": True,
		"aaa": True,
		"jchzalrnumimnmhp": False,
		"haegwjzuvuyypxyu": False,
		"dvszwmarrgswjxmb": False
	}

	for input_str, answer in test_inputs.items():
		if check_if_nice(input_str) != answer:
			print("Input String: {} is wrong".format(input_str))
		else:
			print("Input String: {} passed test".format(input_str))


def new_nice_rules_check(string):
	found_skipped_char = False
	found_second = False
	for i in range(0, len(string) - 1):
		first_char = string[i]
		second_char = string[i + 1]
		third_char = None
		try:
			third_char = string[i + 2]
		except IndexError:
			continue

		if not found_second:
			count = string.count("{}{}".format(first_char, second_char))
			if count > 1:
				found_second = True

		if not found_skipped_char:
			if first_char == third_char:
				found_skipped_char = True
	return found_skipped_char and found_second



def part1():
	answer = 0
	for line in data:
		result = check_if_nice(line)
		if result:
			answer += 1
	print(answer)


def test_new_rules():
	test_data = {
		"qjhvhtzxzqqjkmpb": True,
		"xxyxx": True,
		"uurcxstgmygtbstg": False,
		"ieodomkazucvgmuy": False
	}
	for test_input, result in test_data.items():
		answer = new_nice_rules_check(test_input)
		print("---")
		if answer != result:
			print("PROBLEM")
			print(test_input, result)


def part2():
	answer = 0
	for line in data:
		result = new_nice_rules_check(line)
		if result:
			answer += 1
	print(answer)

def main():
	part2()


if __name__ == '__main__':
	main()