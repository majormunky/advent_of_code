from PIL import Image
from common import get_file_contents


class Point:
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)

	def __str__(self):
		return "Point(x={}, y={})".format(self.x, self.y)

	def __repr__(self):
		return str(self)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y


class Line:
	def __init__(self, start, end):
		self.start = start
		self.end = end
		self.direction = None
		self.find_direction()

	def find_direction(self):
		if self.start.x == self.end.x:
			self.direction = "vertical"
			if self.start.y > self.end.y:
				self.start, self.end = self.end, self.start
		elif self.start.y == self.end.y:
			self.direction = "horizontal"
			if self.start.x > self.end.x:
				self.start, self.end = self.end, self.start
		else:
			rx = abs(self.end.x - self.start.x)
			ry = abs(self.end.y - self.start.y)
			if rx == ry:
				if self.start.x > self.end.x:
					self.start, self.end = self.end, self.start
				self.direction = "diagonal"
			else:
				self.direction = "unknown"


class Board:
	def __init__(self, width, height):
		self.lines = []
		self.grid = None
		self.width = width
		self.height = height
		self.overlaps = 0
		self.diagonal = False
		self.setup_grid()


	def set_diagonal(self, val):
		self.diagonal = val

	def setup_grid(self):
		self.grid = [["." for x in range(self.width)] for y in range(self.height)]

	def add_line(self, new_line):
		# check existing lines for any overlaps
		self.lines.append(new_line)
	
		x = new_line.start.x
		y = new_line.start.y
		if new_line.direction == "horizontal":
			while x <= new_line.end.x:
				self.mark_pos_on_board(x, y)
				x += 1
		elif new_line.direction == "vertical":
			while y <= new_line.end.y:
				self.mark_pos_on_board(x, y)
				y += 1
		elif new_line.direction == "diagonal":
			if self.diagonal:
				while x <= new_line.end.x:
					self.mark_pos_on_board(x, y)
					x += 1
					if y > new_line.end.y:
						y -= 1
					else:
						y += 1
	

	def add_lines(self, line_list):
		for line in line_list:
			self.add_line(line)

	def get_collision_count(self):
		total = 0
		for row_index, row in enumerate(self.grid):
			for col_index, col in enumerate(row):
				if col != "." and col > 1:
					total += 1
		return total

	def mark_pos_on_board(self, x, y):
		try:
			if self.grid[y][x] == ".":
				self.grid[y][x] = 1
			else:
				self.grid[y][x] += 1
		except IndexError:
			print(x, y, len(self.grid), len(self.grid[0]))



def parse_line(line):
	parts = line.split("->")
	start_pos_parts = parts[0].split(",")
	end_pos_parts = parts[1].split(",")
	return Line(Point(*start_pos_parts), Point(*end_pos_parts))


def p1():
	lines = get_file_contents("data/day5_input.txt")
	board_lines = []
	max_x = 0
	max_y = 0
	for line in lines:
		new_line = parse_line(line)
		if new_line.direction != "unknown":
			board_lines.append(new_line)
			max_x = max(max_x, new_line.start.x, new_line.end.x)
			max_y = max(max_y, new_line.start.y, new_line.end.y)

	board = Board(max_x + 40, max_y + 40)
	board.add_lines(board_lines)

	return board.get_collision_count()


def p2():
	lines = get_file_contents("data/day5_input.txt")
	board_lines = []
	max_x = 0
	max_y = 0
	for line in lines:
		new_line = parse_line(line)	
		board_lines.append(new_line)
		max_x = max(max_x, new_line.start.x, new_line.end.x)
		max_y = max(max_y, new_line.start.y, new_line.end.y)

	board = Board(max_x + 40, max_y + 40)
	board.set_diagonal(True)
	board.add_lines(board_lines)
	render_grid(board.grid)
	return board.get_collision_count()


def render_grid(data):
	width = len(data[0])
	height = len(data)
	input_image = Image.new(mode="RGB", size=(width, height), color="white")
	pixel_map = input_image.load()

	total = 0

	for row_index, row in enumerate(data):
		for col_index, col in enumerate(row):
			if col != ".":
				pixel_map[row_index, col_index] = (0, 0, 0)
				if col > 1:
					total += 1

	print("TOTAL", total)

	input_image.save("p2.png", format="png")


if __name__ == '__main__':
	# Not 5331
	# Not 5295
	print("Part 1:", p1())
	print("Part 2:", p2())
