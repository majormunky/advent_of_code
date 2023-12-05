import common


test_data = [
	"seeds: 79 14 55 13",
	"",
	"seed-to-soil map:",
	"50 98 2",
	"52 50 48",
	"",
	"soil-to-fertilizer map:",
	"0 15 37",
	"37 52 2",
	"39 0 15",
	"",
	"fertilizer-to-water map:",
	"49 53 8",
	"0 11 42",
	"42 0 7",
	"57 7 4",
	"",
	"water-to-light map:",
	"88 18 7",
	"18 25 70",
	"",
	"light-to-temperature map:",
	"45 77 23",
	"81 45 19",
	"68 64 13",
	"",
	"temperature-to-humidity map:",
	"0 69 1",
	"1 0 69",
	"",
	"humidity-to-location map:",
	"60 56 37",
	"56 93 4",
]


def parse_data(data):
	seed_line = data[0]
	seed_parts = seed_line.split(":")
	seed_list = seed_parts[-1].strip().split(" ")
	result = {"seeds": seed_list}
	
	new_group = False
	new_group_key = None

	for line in data[1:]:
		if line == "":
			new_group = True
			new_group_key = None
		else:
			if new_group:
				new_group_key = line.replace(" map:", "")
				result[new_group_key] = []
				new_group = False
			else:
				line_parts = line.split(" ")
				dest_value = int(line_parts[0])
				source_value = int(line_parts[1])
				amount_value = int(line_parts[2])

				source_range = range(source_value, source_value + amount_value)
				dest_range = range(dest_value, dest_value + amount_value)
				result[new_group_key].append({
					"source": source_range,
					"dest": dest_range
				})

	return result


def follow_chain(seed_num, data):
	maps = [
		"seed-to-soil",
		"soil-to-fertilizer",
		"fertilizer-to-water",
		"water-to-light",
		"light-to-temperature",
		"temperature-to-humidity",
		"humidity-to-location"
	]

	result_dict = {"seed": seed_num}

	current_value = seed_num
	for i in maps:
		found = False
		for item_range in data[i]:
			try:
				current_value_index = item_range["source"].index(current_value)
				dest_value = item_range["dest"][current_value_index]
				result_dict[i] = dest_value
				current_value = dest_value
				found = True
				break
			except ValueError:
				pass
		if found is False:
			result_dict[i] = current_value

	return result_dict


def part1(debug=True):
	if debug:
		data = test_data
	else:
		data = common.get_file_contents("data/day05_input.txt")

	parsed_data = parse_data(data)


	lowest = 1_000_000_000
	for seed in parsed_data["seeds"]:
		seed_chain = follow_chain(int(seed), parsed_data)
		# print("Seed:", seed, "Location:", seed_chain["humidity-to-location"])
		if seed_chain["humidity-to-location"] < lowest:
			lowest = seed_chain["humidity-to-location"]

	print(lowest)


if __name__ == '__main__':
	part1(False)

