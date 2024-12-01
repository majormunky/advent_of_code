import os
import common


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def build_memory_bank(data):
    result = []
    for item in data.split(" "):
        if len(item) > 0 and item != " ":
            result.append(int(item))
    return result


def get_highest_bank(data) -> int:
    highest = 0
    highest_index = 0
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
    real_file = os.path.join("..", "data", "day05_input.txt")
    data = common.get_file_contents(real_file, single_line=True)

    # list of 16 ints
    memory = build_memory_bank(data)

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
            # write_data(old_memory)
            return steps
        else:
            old_memory.append(list(memory))


def part2():
    real_file = os.path.join("..", "data", "day05_input.txt")
    data = common.get_file_contents(real_file, single_line=True)

    # list of 16 ints
    memory = build_memory_bank(data)

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
            # where in our list is our first time we saw this
            mem_index = old_memory.index(memory)

            # our loop length is our index to the end of our loop
            how_long_ago = len(old_memory) - mem_index
            return how_long_ago
        else:
            old_memory.append(list(memory))


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
