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
        for i in range(len(bucket_names)):
            i_key = i * chunk_size
            if line[i_key] == "[":
                key = str(i + 1)
                data[key].append(line[i_key + 1])

    return data


def render_stacks(data):
    tallest_stack = 50

    bucket_size = len(data)
    lines = []
    for _ in range(tallest_stack):
        lines.append(" " * (bucket_size * 4))

    last_line = " "
    for i in range(1, bucket_size + 1):
        last_line += "{}   ".format(i)
    last_line = last_line.rstrip()
    last_line += " "
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


def step_p2(instruction, data):
    frames = []
    pile = []

    # pick up all crates first
    for _ in range(instruction["amount"]):
        from_pile = data[instruction["from"]]
        crate = from_pile.pop(0)
        pile.append(crate)

    to_pile = data[instruction["to"]]
    data[instruction["to"]] = pile + to_pile
    frames.append(render_stacks(data))
    return frames


def step_p1(instruction, data):
    frames = []
    for _ in range(instruction["amount"]):
        from_pile = data[instruction["from"]]
        crate = from_pile.pop(0)
        to_pile = data[instruction["to"]]
        data[instruction["to"]] = [crate] + to_pile
        frames.append(render_stacks(data))
    return frames


def get_test_lines():
    return [
        "    [D]    \n",
        "[N] [C]    \n",
        "[Z] [M] [P]\n",
        " 1   2   3 \n",
        "\n",
        "move 1 from 2 to 1\n",
        "move 3 from 1 to 3\n",
        "move 2 from 2 to 1\n",
        "move 1 from 1 to 2\n",
    ]


def p1():
    should_render_frames = False
    lines = get_file_contents(
        "data/day05_input.txt", single_line=False, strip_line=False
    )
    data = parse_stack_data(get_stack_data(lines))
    instructions = get_instructions(lines)

    frames = []

    frames.append(render_stacks(data))

    for instruction in instructions:
        frame_list = step_p1(instruction, data)
        frames.extend(frame_list)

    if should_render_frames:
        for index, frame in enumerate(frames):
            os.system("clear")
            sys.stdout.write("frame: " + str(index + 1))
            for line in frame:
                sys.stdout.write(line + "\n")
            sys.stdout.flush()
            time.sleep(0.01)

    result = ""
    for i in range(1, len(data) + 1):
        result += data[str(i)][0]
    print_stacks(frames[-1])
    print(result)


def p2():
    should_render_frames = False
    lines = get_file_contents(
        "data/day05_input.txt", single_line=False, strip_line=False
    )
    data = parse_stack_data(get_stack_data(lines))
    instructions = get_instructions(lines)

    frames = []

    frames.append(render_stacks(data))

    for instruction in instructions:
        frame_list = step_p2(instruction, data)
        frames.extend(frame_list)

    if should_render_frames:
        for index, frame in enumerate(frames):
            os.system("clear")
            sys.stdout.write("frame: " + str(index + 1))
            for line in frame:
                sys.stdout.write(line + "\n")
            sys.stdout.flush()
            time.sleep(0.01)

    result = ""
    for i in range(1, len(data) + 1):
        result += data[str(i)][0]
    print_stacks(frames[-1])
    print(result)


def main():
    p2()


if __name__ == "__main__":
    main()
