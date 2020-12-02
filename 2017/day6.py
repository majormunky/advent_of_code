import os
import sys
import common


def get_filename():
    filename = sys.argv[0]
    filename = filename.split("/")[-1]
    filename = filename.split(".")[0]
    return filename

data = common.get_file_contents("data/{}_input.txt".format(get_filename()), single_line=True)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def build_memory_bank():
    result = []
    for item in data.split(" "):
        if len(item) > 0 and item != " ":
            result.append(int(item))
    return result


def get_highest_bank(data):
    highest = 0
    highest_index = None
    for index, val in enumerate(data):
        if val > highest:
            highest = val
            highest_index = index
    return highest_index


def write_data(lines):
    with open(os.path.join(BASE_DIR, "data/day6_steps.txt"), "w") as f:
        for line in lines:
            line = [str(x) for x in line]
            output = ",".join(line)
            f.write(output + "\n")


def part1():
    # list of 16 ints
    memory = build_memory_bank()
    
    # our cache of old memory
    old_memory = []

    # amount of steps taken
    steps = 0

    while True:
        highest_amount_index = get_highest_bank(memory)
        amount = memory[highest_amount_index]
        memory[highest_amount_index] = 0
        while amount > 0:
            highest_amount_index += 1
            if highest_amount_index >= len(memory):
                highest_amount_index = 0
            memory[highest_amount_index] += 1
            amount -= 1
        steps += 1
        if memory in old_memory:
            write_data(old_memory)
            return steps
        else:
            old_memory.append(list(memory))


def part2():
    return "not complete"


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()

