extends KinematicBody2D


var velocity = Vector2.ZERO
const SPEED = 40

# Called when the node enters the scene tree for the first time.
func _ready():
	velocity = Vector2(SPEED, 0)


func _physics_process(delta):
	velocity = move_and_slide(velocity)


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
