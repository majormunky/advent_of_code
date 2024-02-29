import pprint
import sys
import common

data = common.get_file_contents("data/day8_input.txt")


test_lines = [
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6"
]


def parse_instruction(line):
    parts = line.split(" ")
    amount_parts = list(parts[1])
    plus_or_minus = "plus"

    if amount_parts[0] == "-":
        plus_or_minus = "minus"

    amount_parts.pop(0)
    amount = "".join(amount_parts)
    
    return {
        "type": parts[0],
        "direction": plus_or_minus,
        "amount": int(amount)
    }


def part1():
    accumulator = 0
    index = 0

    max_steps = 20
    steps = 0

    visited_indexes = []

    while True:
        if index in visited_indexes:
            break

        visited_indexes.append(index)
        
        try:
            line = data[index]
        except IndexError:
            print("Index: ", index)
            break
        
        inst = parse_instruction(line)

        inst_type = inst["type"]

        if inst_type == "nop":
            index += 1
        elif inst_type == "acc":
            if inst["direction"] == "plus":
                accumulator += inst["amount"]
            else:
                accumulator -= inst["amount"]
            index += 1
        elif inst_type == "jmp":            
            if inst["direction"] == "plus":
                index += inst["amount"]
            else:
                index -= inst["amount"]

        
    return accumulator


def part2():
    return 0


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == "__main__":
    main()
