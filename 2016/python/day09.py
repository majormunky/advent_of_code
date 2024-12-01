import common
import sys

def get_filename():
    filename = sys.argv[0]
    filename = filename.split("/")[-1]
    filename = filename.split(".")[0]
    return filename

data = common.get_file_contents("data/{}_input.txt".format(get_filename()))

def parse_instruction(val):
    parts = val.split("x")
    return {"char_count": int(parts[0]), "amount": int(parts[1])}

def expand(line, instruction, start_index, end_index):
    result = line[:start_index]
    parsed_instruction = parse_instruction(instruction)
    characters_to_repeat = line[end_index:end_index + parsed_instruction["char_count"]]

    for i in range(parsed_instruction["amount"]):
        result += characters_to_repeat

    parse_pos = len(result)

    # remove the character(s) that we are expanding
    final_end_index = end_index + parsed_instruction["char_count"]
    end_string = line[final_end_index:]

    return [result, end_string]


def parse_p2(line):
    getting_instruction = False
    result = ""
    instruction = ""
    start_index = None
    end_index = None
    completed = True

    for index, char in enumerate(line):
        # if we aren't currently getting an instruction
        # we need to check for a (
        if getting_instruction is False:
            # if we found a (, set our flag
            if char == "(":
                completed = False
                getting_instruction = True
                start_index = index
                # we can skip the rest of this loop
                continue
        else:
            # we are getting an instruction
            # check if we are at a ) yet
            if char == ")":
                # if so, we can unset the flag
                getting_instruction = False
                # we can also set our index flag for the last
                # index of our instruction
                end_index = index + 1

                # we should now perform the instruction
                # and get a new string
                result, rest_to_parse = expand(line, instruction, start_index, end_index)
                line = f"{result}{rest_to_parse}"
                break
            else:
                instruction += char
    if completed:
        return line
    print(line)
    return parse_p2(line)

def parse(line, remaining):
    getting_instruction = False
    result = line
    instruction = ""
    start_index = None
    end_index = None
    rest_to_parse = None

    # go over each character in the input
    for index, char in enumerate(remaining):
        # if we aren't currently getting an instruction
        # we need to check for a (
        if getting_instruction is False:
            # if we found a (, set our flag
            if char == "(":
                getting_instruction = True
                start_index = index
                # we can skip the rest of this loop
                continue
        else:
            # we are getting an instruction
            # check if we are at a ) yet
            if char == ")":
                # if so, we can unset the flag
                getting_instruction = False
                # we can also set our index flag for the last
                # index of our instruction
                end_index = index + 1

                # we should now perform the instruction
                # and get a new string
                result, rest_to_parse = expand(remaining, instruction, start_index, end_index)
                line += result
                remaining = ""
                break
            else:
                instruction += char

    if rest_to_parse:
        return parse(line, rest_to_parse)
    return line + remaining

test_data = {
    "A(1x5)BC": "ABBBBBC",
    "(3x3)XYZ": "XYZXYZXYZ",
    "A(2x2)BCD(2x2)EFG": "ABCBCDEFEFG",
    "(6x1)(1x3)A": "(1x3)A",
    "X(8x2)(3x3)ABCY": "X(3x3)ABC(3x3)ABCY"
}

def part1():
    # result = parse("", "(3x3)XYZ")
    # print(result)
    # print("XYZXYZXYZ")
    answer = 0
    for input_str in data:
        result = parse("", input_str)
        result_len = len(result)
        answer += result_len

    print("Answer:", answer)

def part2():
    result = parse_p2("(27x12)(20x12)(13x14)(7x10)(1x12)A")
    print(result)
    # print("XABCABCABCABCABCABCY")
    # answer = 0
    # for input_str in data:
    #     result = parse_p2(input_str)
    #     result_len = len(result)
    #     answer += result_len

def main():
    # p1 = part1()
    p2 = part2()

    # print("Part 1", p1)
    print("Part 2", p2)

if __name__ == "__main__":
    main()
