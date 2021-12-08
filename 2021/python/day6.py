from common import get_file_contents


def tick(val):
	#print("tick(", val, ")")
	new_fish = False
	if val == 0:
		val = 6
		new_fish = True
	else:
		val -= 1
	#print("end tick", val, new_fish)
	return val, new_fish

def p1():
	lines = get_file_contents("data/day6_input.txt")
	#lines = ['3,4,3,1,2']
	fish = []
	new_fish = []
	for item in lines[0].split(","):
		fish.append(int(item))
	
	days = 80
	for _ in range(days):
		for index, item in enumerate(fish):
			item, create_new_fish = tick(item)
			fish[index] = item
			if create_new_fish:
				new_fish.append(8)
		fish.extend(new_fish)
		new_fish = []

	return len(fish)


def p2():
	"""
	instead of keeping a list of every fish, which ends up growing too fast
	we instead count how many fish we have at each stage.  this lets us process the 
	entire batch of fish in one step, instead of iterating over every fish
	"""
	lines = get_file_contents("data/day6_input.txt")
	#lines = ['3,4,3,1,2']
	fish = {}
	new_fish = []
	for item in lines[0].split(","):
		fish_num = int(item)
		if fish_num not in fish.keys():
			fish[fish_num] = 0
		fish[fish_num] += 1


	days = 256
	for i in range(days):
		new_round = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
		# deal with 0 ones first
	
		# # get the amount of fish that will be respawning
		new_fish_count = fish.get(0, 0)
		
		# # reset the fish back to 6
		new_round[6] = new_fish_count

		# # we also need to spawn a new fish for every fish that we reset
		new_round[8] = new_fish_count

		# deal with the rest
		for num in range(1, 9):
			# take the fish in bucket num and put them into a new bucket that is one less than num
			new_round[num - 1] += fish.get(num, 0)
		
		for k, v in new_round.items():
			if k not in fish.keys():
				fish[k] = 0
			fish[k] = v
	

	fish_count = 0
	for key, val in fish.items():
		fish_count += val

	return fish_count



def p2_slow():
	lines = get_file_contents("data/day6_input.txt")
	#lines = ['3,4,3,1,2']
	fish = []
	new_fish = []
	for item in lines[0].split(","):
		fish.append(int(item))
	
	days = 256
	for x in range(days):
		print("Day", x)
		for index, item in enumerate(fish):
			item, create_new_fish = tick(item)
			fish[index] = item
			if create_new_fish:
				new_fish.append(8)
		fish.extend(new_fish)
		print("Fish:", len(fish))
		new_fish = []

	return len(fish)


if __name__ == '__main__':
	print("Part 1:", p1())
	print("Part 2:", p2())
