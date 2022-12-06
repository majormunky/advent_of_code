import time
import sys
import os
from common import get_file_contents


def get_stack_data(lines):
    result = []

    for line in lines:
        if line == "\n":
            break
        line = line.replace("\n", "")
        result.append(line)
    return result


def parse_stack_data(lines):
    data = {}
    bucket_names = [x for x in lines[-1].split(" ") if len(x) > 0]
    for i in bucket_names:
        data[i] = []

    chunk_size = 4
    for line in lines:
        for i in range(9):
            if line[i * chunk_size] == "[":
                key = str(i + 1)
                data[key].append(line[(i * chunk_size) + 1])

    return data


def render_stacks(data):
    tallest_stack = 50

    # for i in range(1, 10):
    #     stack_height = len(data[str(i)])
    #     if stack_height > tallest_stack:
    #         tallest_stack = stack_height

    lines = []
    for _ in range(tallest_stack):
        lines.append(" " * (9 * 4))

    last_line = " 1   2   3   4   5   6   7   8   9 "
    lines.append(last_line)

    for k, v in data.items():
        start_index = (int(k) - 1) * 4
        fixed_list = list(reversed(v))
        current_index = len(lines) - 2
        for item in fixed_list:
            line_to_work_on = list(lines[current_index])
            line_to_work_on[start_index] = "["
            line_to_work_on[start_index + 1] = item
            line_to_work_on[start_index + 2] = "]"
            lines[current_index] = "".join(line_to_work_on)
            current_index -= 1
    return lines


def print_stacks(data):
    for line in data:
        print(line)


def get_instructions(lines):
    result = []

    found_blank_row = False

    for line in lines:
        if line == "\n":
            found_blank_row = True
            continue

        if found_blank_row:
            parsed_instruction = parse_instruction(line.strip())
            result.append(parsed_instruction)
    return result


def parse_instruction(inst):
    parts = inst.split(" ")
    result = {"from": parts[3], "to": parts[5], "amount": int(parts[1])}
    return result


def step(instruction, data):
    frames = []
    for _ in range(instruction["amount"]):
        crate = data[instruction["from"]].pop()
        data[instruction["to"]].append(crate)
        frames.append(render_stacks(data))
    return frames


def p1():
    lines = get_file_contents(
        "data/day05_input.txt", single_line=False, strip_line=False
    )
    data = parse_stack_data(get_stack_data(lines))
    instructions = get_instructions(lines)

    frames = []

    frames.append(render_stacks(data))

    for instruction in instructions:
        frames.extend(step(instruction, data))

    print(len(frames))

    # parse_stack_data(top_part)
    # print_stacks(top_part)

    for index, frame in enumerate(frames):
        os.system("clear")
        sys.stdout.write("frame: " + str(index + 1))
        for line in frame:
            sys.stdout.write(line + "\n")
        sys.stdout.flush()
        time.sleep(0.01)


def p2():
    pass


def main():
    p1()


if __name__ == "__main__":
    main()
