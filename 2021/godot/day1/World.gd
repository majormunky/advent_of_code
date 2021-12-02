extends Node2D

onready var line = $Line2D


func _ready():
	var points = get_points()
	
	var x_pos = 0
	
	var min_point = 100000
	var max_point = 0
	
	print("Points Loaded: ", len(points))
	
	for y_pos in points:
		y_pos = int(y_pos)

		if y_pos < min_point:
			print("found new min, current: ", min_point, " new: ", y_pos)
			min_point = y_pos
	
		if y_pos > max_point:
			max_point = y_pos

		line.add_point(Vector2(x_pos, y_pos))
		x_pos += 10
	
	print("Min: ", min_point, " Max: ", max_point)


func get_points():
	var data_file = File.new()
	data_file.open("res://data/day1_data.txt", File.READ)
	var content = data_file.get_as_text()
	var lines = content.split("\n")
	data_file.close()
	return lines
