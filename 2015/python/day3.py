import common


def part1():
	data = common.get_file_contents("data/day3_input.txt")[0]
	houses = set()
	x = 0
	y = 0

	houses.add((x, y))
	for char in data:
		if char == ">":
			x += 1
		elif char == "<":
			x -= 1
		elif char == "^":
			y -= 1
		elif char == "v":
			y += 1
		
		pos = (x, y)
		houses.add(pos)

	print(len(houses))


def part2():
	data = common.get_file_contents("data/day3_input.txt")[0]
	turn = "santa"
	workers = {
		"santa": [0, 0],
		"robo": [0, 0]
	}
	houses = set()
	houses.add((0, 0))

	directions = {
		">": (1, 0),
		"<": (-1, 0),
		"^": (0, -1),
		"v": (0, 1)
	}

	for char in data:
		offset = directions[char]

		workers[turn][0] += offset[0]
		workers[turn][1] += offset[1]

		houses.add((workers[turn][0], workers[turn][1]))

		if turn == "santa":
			turn = "robo"
		else:
			turn = "santa"

	print(len(houses))



def main():
	part2()


if __name__ == '__main__':
	main()