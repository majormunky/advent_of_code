import common


data = common.get_file_contents("data/day6_input.txt")


def main():
	part1()


def part2():
	pass


def test_change_list(l):
	l[2] = 10
	return l


def parse_instruction(i):
	parts = i.split(" ")

	action = None
	if i.startswith("turn off"):
		action = "turn off"
	elif i.startswith("turn on"):
		action = "turn on"
	elif i.startswith("toggle"):
		action = "toggle"

	start_pos_parts = parts[-3].split(",")
	end_pos_parts = parts[-1].split(",")

	start_pos = (int(start_pos_parts[0]), int(start_pos_parts[1]))
	end_pos = (int(end_pos_parts[0]), int(end_pos_parts[1]))

	return {
		"action": action,
		"start_pos": start_pos,
		"end_pos": end_pos
	}


def update_grid(step, g):
	for y in range(step["start_pos"][1], step["end_pos"][1] + 1):
		for x in range(step["start_pos"][0], step["end_pos"][0] + 1):
			action = step["action"]
			if action == "turn on":
				g[y][x] = True
			elif action == "turn off":
				g[y][x] = False
			elif action == "toggle":
				if g[y][x]:
					g[y][x] = False
				else:
					g[y][x] = True
	return g


def count_lights(g):
	lights = 0
	for row in g:
		for item in row:
			if item:
				lights += 1
	return lights


def part1():
	# setup a 2d grid of false values to represent lights
	grid = [[False for x in range(1000)] for y in range(1000)]

	for instruction in data:
		# parse the line into a dictionary
		step_data = parse_instruction(instruction)

		# update the grid with our instruction
		grid = update_grid(step_data, grid)

	answer = count_lights(grid)
	print(answer)


if __name__ == '__main__':
	main()
