from common import get_file_contents


def get_data(debug=False):
	debug_data = """
		5483143223
		2745854711
		5264556173
		6141336146
		6357385478
		4167524645
		2176841721
		6882881134
		4846848554
		5283751526
	"""
	debug_data_mini = """
		11111
		19991
		19191
		19991
		11111
	"""
	if debug:
		result = []
		for line in debug_data.split("\n"):
			if len(line) > 1:
				result.append(line.strip())
		return result
	else:
		return get_file_contents("data/day11_data.txt")


def print_grid(grid):
	for row in grid:
		print(str(row))
	print("----")


def add_energy_step(old_step):
	new_step = []
	for row_index, row in enumerate(old_step):
		new_step.append([])
		for col_index, col in enumerate(row):
			new_step[row_index].append(int(col) + 1)
	return new_step


def lines_to_grid(lines):
	result = []
	for row in lines:
		new_row = []
		for char in list(row):
			new_row.append(int(char))
		result.append(new_row)
	return result


def get_neighbors(x, y, width, height):
	result = []
	if x > 0 and y > 0:
		result.append([x - 1, y - 1]) # upper left

	if y > 0:
		result.append([x, y - 1])     # top

	if x < width and y > 0:
		result.append([x + 1, y - 1]) # upper right
	
	if x > 0:
		result.append([x - 1, y])     # left
	
	if x < width:
		result.append([x + 1, y])     # right
	
	if x > 0 and y < height:
		result.append([x - 1, y + 1]) # lower left
	
	if y < height:
		result.append([x, y + 1])     # bottom
	
	if x < width and y < height:
		result.append([x + 1, y + 1]) # lower right
	return result


def check_for_flashes(grid):
	debug = True
	blinks = 0
	done = False
	rounds = 0
	total_items = len(grid) * len(grid[0])
	print("Total Items:", total_items)

	grid_width = len(grid[0])
	grid_height = len(grid)
	blinks_this_round = 0

	# during the process of flashing, we may introduce more flashes
	# so we need to loop an unknown amount of times, until there
	# are no more flashes
	while not done:
		rounds += 1
		did_flash = False
		
		if debug:
			print("Round", rounds)
			print_grid(grid)
		for row_index, row in enumerate(grid):
			for col_index, col in enumerate(row):
				if col > 9:
					# blink
					blinks += 1
					blinks_this_round += 1

					# get list of neighbors
					neighbor_list = get_neighbors(
						col_index,
						row_index,
						grid_width,
						grid_height
					)
					
					for neighbor in neighbor_list:
						try:
							# if the neighbor has a 0
							# then we should not do anything with that
							# as its already blinked and been reset
							nx, ny = neighbor
							if grid[ny][nx] > 0:
								grid[ny][nx] += 1
								if grid[ny][nx] > 9:
									pass
						except IndexError:
							pass

					# set energy level to 0
					grid[row_index][col_index] = 0

					# mark that we did flash at least something on this round
					did_flash = True
		if debug:
			print("After Round")
			print_grid(grid)
		print("Blinks this round:", blinks_this_round)
		if blinks_this_round == total_items:
			print("All items flashed!!!!!!!!!!!!!!!!")
			return None, None
		if blinks_this_round == 99:
			print_grid(grid)
		if not did_flash:
			# if we didn't flash, we can stop
			done = True
	print("Rounds", rounds)
	return blinks, grid
					


def perform_steps(amount, grid):
	flash_count = 0
	# print("Before any steps")
	# print_grid(grid)
	for i in range(amount):
		print("Step", str(i + 1))
		grid = add_energy_step(grid)
		# print("After Energy Step")
		# print_grid(grid)
		flashes, grid = check_for_flashes(grid)
		if flashes:
			flash_count += flashes
		elif flashes is None and grid is None:
			break
		# print("Flashes:", flashes)
		# print("Total Flashes:", flash_count)
		# print_grid(grid)



def p1():
	lines = get_data()
	grid = lines_to_grid(lines)
	perform_steps(100, grid)


def p2():
	lines = get_data()
	grid = lines_to_grid(lines)
	perform_steps(500, grid)


if __name__ == '__main__':
	# print("Part 1:", p1())
	print("Part 2:", p2())
