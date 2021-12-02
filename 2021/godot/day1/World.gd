extends Node2D

onready var line = $Line2D

func _ready():
	var points = [
		200,
		208,
		199,
		213,
		190,
		189,
		200,
		202
	]
	
	var x_pos = 0
	
	for y_pos in points:
		line.add_point(Vector2(x_pos, y_pos))
		x_pos += 10
