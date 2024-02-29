import pprint
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


def find_gold_holding_bags(data):
    result = {}
    for line in data:
        parts = line.split("contain")
        if len(line) == 0:
            continue
        holding_bag = parts[0].replace("bags", "bag").strip()
        bags_being_held = {}
        for bag in parts[1].split(","):
            bag = bag.strip()
            if "no other bags." not in bag:
                bag_parts = bag.split(" ")
                bag_parts.pop(0)
                fixed_bag_name = " ".join(bag_parts)
                fixed_bag_name = fixed_bag_name.replace(".", "").replace("bags", "bag")
                bags_being_held[fixed_bag_name] = {}
        result[holding_bag] = bags_being_held

    for k, v in result.items():
        # print(k)
        for subk, subv in v.items():
            # print("\t", subk, subv)
            if subk in result.keys() and subk != "shiny gold bag":
                result[k][subk] = result[subk]
                # print("\t\t!", result[subk])

    return result


def check_bag_for_gold(bag_data):
    test = str(bag_data)
    if "shiny gold" in test:
        return True
    return False


def part1():
    # first we arrange our data in layers of dicts
    bags = find_gold_holding_bags(data)

    # this will hold our bag names that contain shiny gold bags
    result = set()

    # check each bag
    for key in bags.keys():
        # this checks if the string "shiny gold" is in the dictionary
        if check_bag_for_gold(bags[key]):
            # if so, add our key
            result.add(key)

    # the answer is the amount of results we've added
    return len(result)


def parse_bag_data(lines):
    result = {}

    for line in lines:
        if line == "":
            continue
        parts = line.split("contain")
        main_bag_name = parts[0].replace("bags", "").strip()
        other_bags = parts[1].split(",")

        result[main_bag_name] = {}

        if "no other bags" in parts[1]:
            continue

        for other_bag in other_bags:
            other_bag_parts = other_bag.split(" ")
            amount = int(other_bag_parts.pop(1))

            other_bag_parts.pop(0)
            other_bag_parts.pop()

            other_bag_name = " ".join(other_bag_parts)
            result[main_bag_name][other_bag_name] = amount

    return result


def part2():
    bags = parse_bag_data(data)

    bags_to_check = ["shiny gold"]

    total_bags = 0

    while bags_to_check:
        total_bags += 1
        next_bag = bags_to_check.pop()
        for bag_name, bag_amount in bags[next_bag].items():
            for i in range(bag_amount):
                bags_to_check.append(bag_name)

    total_bags -= 1

    return total_bags


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == "__main__":
    main()
