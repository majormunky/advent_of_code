import os
import common


def run_program(lines):
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

    return result


def p1():
    # test_lines = [
    #     "noop",
    #     "addx 3",
    #     "addx -5",
    # ]

    real_file = os.path.join("..", "data", "day10_input.txt")
    lines = common.get_file_contents(real_file)

    result = run_program(lines)
    check_keys = [20, 60, 100, 140, 180, 220]

    answer = 0
    for k in check_keys:
        answer += result[k] * k
    # Answer: 11960
    print(answer)


def p2():
    # test_file = os.path.join("..", "data", "data/day10_test.input")
    real_file = os.path.join("..", "data", "day10_input.txt")
    lines = common.get_file_contents(real_file)

    result = run_program(lines)
    cycle_count = len(result.keys())
    output = ""

    row_length = 40
    current_row = 0
    col_counter = 0

    for index in range(cycle_count):
        cycle = index + 1
        x = result[cycle]

        row_diff = row_length * current_row
        index -= row_diff

        cycle_diff = abs(int(index) - int(x))

        print(cycle, x, row_diff, cycle_diff)

        if cycle_diff < 2:
            output += "#"
        else:
            output += "."

        col_counter += 1
        if col_counter >= row_length:
            col_counter = 0
            current_row += 1
    # Answer: EJCFPGLH
    print_answer(output)



def print_answer(output):
    print(output[0:40])
    print(output[40:80])
    print(output[80:120])
    print(output[120:160])
    print(output[160:200])
    print(output[200:240])


def main():
    p1()
    p2()


if __name__ == "__main__":
    main()
