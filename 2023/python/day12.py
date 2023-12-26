import common

test_data = [
	"???.### 1,1,3",
	".??..??...?##. 1,1,3",
	"?#?#?#?#?#?#?#? 1,3,1,6",
	"????.#...#... 4,1,1",
	"????.######..#####. 1,6,5",
	"?###???????? 3,2,1"
]

def get_data(debug, data):
	if debug:
		data = list(data)
	else:
		data = common.get_file_contents("data/day12_input.txt")
	return data


def generate_spring_configurations(springs):
	for spring in springs:
		spring_list = list(spring)
		for char_index, char in enumerate(spring_list):
			if char == "?":
				test_1 = list(spring)
				test_2 = list(spring)

				test_1[char_index] = "#"
				test_2[char_index] = "."

				test_1_string = "".join(test_1)
				test_2_string = "".join(test_2)

				# print(test_1_string, test_2_string)

				springs.extend(generate_spring_configurations([test_1_string]))
				springs.extend(generate_spring_configurations([test_2_string]))

				return springs

	return springs


def process_line(line):
	data = line.split(" ")

	counts = []
	for count in data[1].split(","):
		counts.append(int(count))

	springs = data[0]

	# print(springs)

	options = generate_spring_configurations([springs])

	# print(options)

	test_springs = []

	for option in options:
		if "?" not in option and is_valid_data(option, counts):
			test_springs.append(option)

	# print(test_springs)

	return len(test_springs)



def is_valid_data(springs, spring_data):
	temp_parts = springs.split(".")
	parts = []

	for p in temp_parts:
		if p != "":
			parts.append(p)

	if len(parts) != len(spring_data):
		return False

	for index, amount in enumerate(spring_data):
		if len(parts[index]) != amount:
			return False

	return True


def part1(debug=True):
    lines = get_data(debug, test_data)
    # process_line(lines[1])
    result = 0
    for line in lines:
    	result += process_line(line)
    print(result)


def part2(debug=True):
    lines = get_data(debug, test_data)


if __name__ == "__main__":
    part1(False) # 7916
    part2()
