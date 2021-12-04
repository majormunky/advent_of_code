extends Node2D

onready var line = $Line2D
onready var path = $Path2D
onready var path_follow = $Path2D/PathFollow2D
onready var submarine = $Path2D/PathFollow2D/Submarine

func _process(delta):
	path_follow.offset += 25 * delta


func _ready():
	var points = get_points()
	
	var x_pos = 0
	
	var min_point = 100000
	var max_point = 0
	
	print("Points Loaded: ", len(points))
	
	submarine.global_position = Vector2(0, points[0])
	
	for y_pos in points:
		y_pos = int(y_pos)

		if y_pos < min_point:
			print("found new min, current: ", min_point, " new: ", y_pos)
			min_point = y_pos
	
		if y_pos > max_point:
			max_point = y_pos

		var new_point = Vector2(x_pos, y_pos)
		line.add_point(new_point)
		path.curve.add_point(new_point)
		x_pos += 10
	
	print("Min: ", min_point, " Max: ", max_point)


func get_points():
	var data_file = File.new()
	data_file.open("res://data/day1_data.txt", File.READ)
	var content = data_file.get_as_text()
	var lines = content.split("\n")
	data_file.close()
	return lines
