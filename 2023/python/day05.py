import time
import common
import sys


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

	# result_dict = {"seed": seed_num}

	current_value = seed_num
	for i in maps:
		found = False
		for item_range in data[i]:
			try:
				current_value_index = item_range["source"].index(current_value)
				dest_value = item_range["dest"][current_value_index]
				# result_dict[i] = dest_value
				current_value = dest_value
				found = True
				break
			except ValueError:
				# result_dict[i] = current_value
				pass

	return current_value


def build_chain(data):
	"""
	Build map from seed num to location num
	"""
	result = {}

	for seed_range in data["seed-to-soil"]:
		for seed_source_num in seed_range["source"]:
			seed_chain = follow_chain(seed_source_num, data)
			result[seed_source_num] = seed_chain

	return result


def get_seed_ranges(data):
	seeds = data["seeds"]

	seed_start = None

	result = []

	for seed in seeds:
		if seed_start is None:
			seed_start = int(seed)
		else:
			seed_range = range(seed_start, int(seed_start + int(seed)))
			result.append(seed_range)
			seed_start = None

	return result


def part1(debug=True):
	if debug:
		data = test_data
	else:
		data = common.get_file_contents("data/day05_input.txt")

	parsed_data = parse_data(data)
	print("Data parsed")
	print(parsed_data)

	seed_map = build_chain(parsed_data)
	print("Chain pre-computed")
	# print(seed_map)

	lowest = 1_000_000_000
	for seed in parsed_data["seeds"]:
		print(seed)
		# seed_chain = follow_chain(int(seed), parsed_data)
		# # print("Seed:", seed, "Location:", seed_chain["humidity-to-location"])
		# if seed_chain < lowest:
		# 	lowest = seed_chain
		seed_int = int(seed)
		if seed_int in seed_map.keys():
			seed_location = seed_map[int(seed)]
		else:
			print(f"Unable to find seed {seed_int} in cache, computing")
			seed_location = follow_chain(seed_int, parsed_data)

		if seed_location < lowest:
			lowest = seed_location

	print(lowest)


def part2_slow(debug=True):
	if debug:
		data = test_data
	else:
		data = common.get_file_contents("data/day05_input.txt")

	parsed_data = parse_data(data)

	seed_ranges = get_seed_ranges(parsed_data)

	lowest = 1_000_000_000
	chains_completed = 0
	# for seed_range in seed_ranges:
	print("seed length:", len(seed_ranges[0]))
	for s in seed_ranges[0]:

		seed_chain = follow_chain(s, parsed_data)
		chains_completed += 1
		
		if chains_completed % 10000 == 0:
			print("Chains Completed: ", chains_completed)
		if seed_chain < lowest:
			lowest = seed_chain
	print("Seed Range Completed")
	print(lowest)


class FancyDict():
	def __init__(self):
		self.source_ranges = []
		self.dest_ranges = []

	def add(self, source, dest):
		self.source_ranges.append(source)
		self.dest_ranges.append(dest)

	def get(self, val):
		for range_index, r in enumerate(self.source_ranges):
			if val in r:
				source_index = self.source_ranges[range_index].index(val)
				return self.dest_ranges[range_index][source_index]
		return val


def build_fancy_dicts(data):
	maps = [
		"seed-to-soil",
		"soil-to-fertilizer",
		"fertilizer-to-water",
		"water-to-light",
		"light-to-temperature",
		"temperature-to-humidity",
		"humidity-to-location"
	]

	result = {}

	for m in maps:
		result[m] = FancyDict()
		for range_item in data[m]:
			result[m].add(range_item["source"], range_item["dest"])

	return result


def follow_fancy_chain(num, data):
	maps = [
		"seed-to-soil",
		"soil-to-fertilizer",
		"fertilizer-to-water",
		"water-to-light",
		"light-to-temperature",
		"temperature-to-humidity",
		"humidity-to-location"
	]

	cur_val = num

	for m in maps:
		cur_val = data[m].get(cur_val)

	return cur_val


def in_cache(range_val):
	existing_lines = []
	cache_name = "day5-cache.txt"
	with open(cache_name, "r") as f:
		for line in f.readlines():
			existing_lines.append(line.strip())

	range_str = f"{range_val[0]}-{range_val[-1]}"

	has_value = False
	for line in existing_lines:
		parts = line.split(":")
		if parts[0] == range_str:
			has_value = True

	return has_value


def write_cache(range_val, lowest):
	cache_name = "day5-cache.txt"
	
	range_str = f"{range_val[0]}-{range_val[-1]}"
	with open(cache_name, "a") as f:
		f.write(f"{range_str}:{lowest}\n")


def part2():
	debug = False
	if debug:
		data = test_data
	else:
		data = common.get_file_contents("data/day05_input.txt")

	parsed_data = parse_data(data)

	generated_data = build_fancy_dicts(parsed_data)

	# seed_range = range(768975, 768975 + 36881621)
	seed_ranges = get_seed_ranges(parsed_data)

	lowest = 1_000_000_000_000_000_000

	for seed_range in seed_ranges:
		print(f"Checking {seed_range}")
		start_time = time.time()
		if not in_cache(seed_range):
			for seed in seed_range:
				result = follow_fancy_chain(seed, generated_data)
				if result < lowest:
					lowest = result
			write_cache(seed_range, lowest)
			print("Wrote to cache", seed_range, lowest)
			end_time = time.time() - start_time
			print(f"Took {end_time} seconds")
		else:
			print("Seed range in cache, skipping")
		
	print(lowest)


if __name__ == '__main__':
	part1() 
	part2(False) # 31161857
