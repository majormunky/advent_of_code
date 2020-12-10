import sys
import common


def get_filename():
    filename = sys.argv[0]
    filename = filename.split("/")[-1]
    filename = filename.split(".")[0]
    return filename


data = common.get_file_contents("data/{}_input.txt".format(get_filename()))
test_data = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""


"""
bright white bags contain 1 shiny gold bag.


1: Find bags that can directly hold gold bags,
	add them to the dictionary.  Key is bag name, 
	value a dictionary holding an amount of gold bags
	and if this bag should be checked into next loop
	This will allow us to be sure we walk down the tree correctly
2: Find any bags that can hold any bags we are tracking,
	if so, add them to our dictionary, and set existing keys to not being tracked
"""

bags = {
	"bright white bags": {"amount": 1, "tracked": True},
	"muted yellow bags": {"amount": 2, "tracked": True}
}


def find_direct_gold_holding_bags(data):
	result = {}
	for line in data:
		parts = line.split("contain")
		if len(line) == 0:
			continue
		holding_bag = parts[0]
		bags_being_held = []
		for bag in parts[1].split(","):
			bag = bag.strip()
			if "no other bags." not in bag:
				bag_data = []
				bag_parts = bag.split(" ")
				bag_data.append(int(bag_parts.pop(0)))
				bag_parts.pop()
				fixed_bag_name = " ".join(bag_parts)
				fixed_bag_name = fixed_bag_name.replace(".", "")
				bag_data.append(fixed_bag_name)
				bags_being_held.append(bag_data)
		result[holding_bag] = bags_being_held
	return result

def part1():
    bags = find_direct_gold_holding_bags(test_data.split("\n"))
    print(bags)


def part2():
    return "not done"
    

def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
