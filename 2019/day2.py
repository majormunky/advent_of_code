import os
import sys
from common import DATA_DIR, get_file_lines


def fix_data(string_list):
    result = []
    for item in string_list[0].split(","):
        result.append(int(item))
    return result


def arrange_operations(data):
    result = []
    temp_list = []
    for code in data:
        if len(temp_list) == 4:
            # take care of full list
            result.append(list(temp_list))

            # reset our list
            temp_list = []

            # check to see if this new code is 99
            # if it is, we need to just add it
            if code == 99:
                result.append([99])
            else:
                # our new code is not 99
                # so just add it to our new list
                temp_list.append(code)
        else:
            # add our code to the list
            temp_list.append(code)
    return result


def arrange_operations_old(data):
    # organize our flat list of instructions into operations
    result = []
    temp_list = []
    for code in data:
        if code == 99:
            if temp_list:
                # we ran into 99 early, put our partial list in our result
                result.append(list(temp_list))
                # then we can add our 99 list
                result.append([99])

                # reset the temp_list
                temp_list = []
        else:
            if len(temp_list) == 3:
                temp_list.append(int(code))
                result.append(list(temp_list))
                temp_list = []
            else:
                temp_list.append(code)
                
    # check to see if our last list was less than a full one
    if temp_list:
        # it was, add it
        result.append(temp_list)
    return result


def run(operation, data):
    if operation[0] == 1:
        num1 = data[operation[1]]
        num2 = data[operation[2]]
        result = int(num1) + int(num2)
        data[operation[3]] = result
    elif operation[0] == 2:
        num1 = data[operation[1]]
        num2 = data[operation[2]]

        result = int(num1) * int(num2)
        data[operation[3]] = result
    elif operation[0] == 99:
        pass
    else:
        print("UNKNOWN OP")
        sys.exit(1)
    return data


def load_data(noun, verb):
    filepath = os.path.join(DATA_DIR, "day2-input.txt")
    lines = get_file_lines(filepath)
    line_parts = fix_data(lines)
    line_parts[1] = noun
    line_parts[2] = verb
    return line_parts


def test(noun, verb, result):
    test_num = calculate_result(noun, verb)
    if test_num == result:
        return True
    return False

def calculate_result(noun, verb):
    line_parts = load_data(noun, verb)
    ops = arrange_operations(line_parts)
    for op in ops:
        run(op, line_parts)
    return line_parts[0]

def part1():
    result = calculate_result(12, 2)
    return result

def part2():
    answer = 19690720
    for y in range(0, 100):
        for x in range(0, 100):
            result = test(x, y, answer)
            if result:
                return x * 100 + y


def main():
    print("Answer for part 1: {}".format(part1()))
    print("Answer for part 2: {}".format(part2()))

if __name__ == "__main__":
    main()
