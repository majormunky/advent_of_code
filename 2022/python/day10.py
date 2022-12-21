from common import get_file_contents


def p1():
    test_lines = [
        "noop",
        "addx 3",
        "addx -5",
    ]

    lines = get_file_contents("data/day10_input.txt")

    x = 1
    cycle_delay = 0
    arg_to_add = None
    instruction_index = 0
    current_instruction = None
    cycles = 0

    result = {}
    
    while True:
        # First thing we do is increment the cycle count
        cycles += 1
        # print(f"Start of cycle: {cycles}, x: {x}")

        # we then set what our current value of x is during this cycle
        result[cycles] = x

        # next, we check to see if our instruction is None
        # if so, it means that we just finished the last instruction
        if current_instruction is None:
            if len(lines) <= instruction_index:
                break
            current_instruction = lines[instruction_index]
            instruction_index += 1

            # if the instruction is a noop, we can just reset things now
            if current_instruction == "noop":
                current_instruction = None
        else:
            _, amount = current_instruction.split(" ")
            x += int(amount)
            current_instruction = None
        # print(f"End of cycle: {cycles}, x: {x}")

    check_keys = [20, 60, 100, 140, 180, 220]

    answer = 0
    for k in check_keys:
        answer += result[k] * k
    # Answer: 11960
    print(answer)


def p2():
    pass


def main():
    p1()


if __name__ == "__main__":
    main()
