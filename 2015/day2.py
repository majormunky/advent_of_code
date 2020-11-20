import common


def get_ribbon_length(width, length, height):
	vals = [width, length, height]
	max_val = max(vals)
	vals.remove(max_val)
	result = vals[0] * 2 + vals[1] * 2
	result += width * length * height
	return result


def get_area(width, length, height):
	side1 = 2 * length * width
	side2 = 2 * width * height
	side3 = 2 * height * length

	small_area = min(side1, side2, side3) // 2

	return side1 + side2 + side3 + small_area


def part1():
	data = common.get_file_contents("data/day2_input.txt")

	result = 0
	for line in data:
		parts = line.split("x")
		result += get_area(int(parts[0]), int(parts[1]), int(parts[2]))
	print(result)


def part2():
	data = common.get_file_contents("data/day2_input.txt")
	result = 0

	for line in data:
		parts = line.split("x")
		result += get_ribbon_length(int(parts[0]), int(parts[1]), int(parts[2]))
	print(result)


def main():
	part2()

if __name__ == '__main__':
	main()