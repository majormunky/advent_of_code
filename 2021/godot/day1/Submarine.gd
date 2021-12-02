extends KinematicBody2D

onready var ray = $RayCast2D
var velocity = Vector2.ZERO
var current_y
var collide_point_y = null
const SPEED = 40

# Called when the node enters the scene tree for the first time.
func _ready():
	current_y = global_position.y
	velocity = Vector2(SPEED, 0)


func _physics_process(delta):
	var line_point = ray.get_collision_point()
	print(ray.is_colliding())
	print(line_point)
	if collide_point_y == null:
		collide_point_y = line_point.y
	else:
		if collide_point_y < line_point.y:
			collide_point_y = line_point.y
			velocity.y = 10
		elif collide_point_y > line_point.y:
			collide_point_y = line_point.y
			velocity.y = -10
	velocity = move_and_slide(velocity)


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
