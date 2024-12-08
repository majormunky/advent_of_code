import os
import common


def find_arguments(instruction):
    args = []
    status = "first"
    tmp_num = ""
    # skip over mul(
    for i in instruction[4:]:
        if i.isdigit():
            tmp_num += i
        elif i == ",":
            if status == "first" and len(tmp_num):
                args.append(int(tmp_num))
                tmp_num = ""
                status = "second"
            else:
                return False
        elif i == ")":
            if status == "second" and len(tmp_num):
                args.append(int(tmp_num))
                return args
        else:
            return False
    return False


def find_muls(instructions):
    result = []

    start = 0

    while True:
        if start >= len(instructions):
            break

        found = instructions.find("mul(", start)
        if found == -1:
            break

        args = find_arguments(instructions[found:])
        if args:
            result.append(args)
        start = found + 1
    return result


def find_muls_part2(instructions, mul_enabled):
    inst_len = len(instructions)

    result = []

    for i in range(inst_len):
        char = instructions[i]
        if char == "d":
            # check for do or don't
            if instructions[i:].startswith("do()"):
                mul_enabled = True
            elif instructions[i:].startswith("don't()"):
                mul_enabled = False
        elif char == "m":
            # check if we have a mul(
            if instructions[i:].startswith("mul(") and mul_enabled:
                args = find_arguments(instructions[i:])
                if args:
                    result.append(args)
    return result, mul_enabled


def part1():
    real_file = os.path.join("..", "data", "day03_input.txt")
    lines = common.get_file_contents(real_file)

    answer = 0

    for line in lines:
        muls = find_muls(line)
        for i in muls:
            answer += i[0] * i[1]

    return answer


def part2():
    real_file = os.path.join("..", "data", "day03_input.txt")
    # test_file = os.path.join("..", "data", "day03_sample_part2.txt")
    lines = common.get_file_contents(real_file)

    answer = 0
    mul_enabled = True
    for line in lines:
        muls, mul_enabled = find_muls_part2(line, mul_enabled)
        for i in muls:
            answer += i[0] * i[1]
    return answer


if __name__ == "__main__":
    part1_answer = part1()

    # too high
    # 78965138
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")
