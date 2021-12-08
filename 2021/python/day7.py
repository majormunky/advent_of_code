from common import get_file_contents


def split_items(data, separator=",", as_int=False):
	converter = int if as_int else lambda x: x
	result = []
	for item in data.split(separator):
		result.append(converter(item))
	return result


def get_fuel_usage_old(crab_list, target):
	fuel = 0
	for crab in crab_list:
		fuel += abs(crab - target)
	return fuel


def get_fuel_usage_new(crab_list, target):
	fuel = 0
	for crab in crab_list:
		steps = abs(crab - target)
		fuel_cost = 1
		for x in range(steps):
			fuel += fuel_cost
			fuel_cost += 1
	return fuel

def p1():
	data = get_file_contents("data/day7_input.txt")[0]
	items = split_items(data, as_int=True)

	lowest = 1_000_000_000
	lowest_target = None
	
	for i in range(max(items)):
		usage = get_fuel_usage_old(items, i)
		if usage < lowest:
			lowest = usage
			lowest_target = i

	print(lowest, lowest_target)

def p2():
	data = get_file_contents("data/day7_input.txt")[0]
	items = split_items(data, as_int=True)

	lowest = 1_000_000_000
	lowest_target = None
	
	for i in range(max(items)):
		usage = get_fuel_usage_new(items, i)
		if usage < lowest:
			lowest = usage
			lowest_target = i

	print(lowest, lowest_target)


if __name__ == '__main__':
	print("Part 1:", p1())
	print("Part 2:", p2())
