import common


test_data = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45",
]


def get_data(debug):
    if debug:
        data = test_data
    else:
        data = common.get_file_contents("data/day09_input.txt")
    return data


def print_data(data):
    i = 0

    for line in data:
        output = " " * i
        for num in line:
            output += f"{num}"
            space_count = min((len(str(num)) + 2), 3)
            output += space_count * " "
            # print(space_count)
        print(output)
        i += 2


def get_differences(values):
    line_length = len(values)

    result = []

    for i in range(line_length - 1):
        result.append(values[i + 1] - values[i])

    return result


def test_differences(values):
    result = True

    for value in values:
        if value != 0:
            result = False

    return result


def calculate(lines):
    lines[-1].append(0)

    data_length = len(lines)

    for line_index in reversed(range(data_length - 1)):
        new_value = lines[line_index][-1] + lines[line_index + 1][-1]
        lines[line_index].append(new_value)

    return lines


def process_line(line):
    data = []

    start_line = []
    for item in line.split(" "):
        start_line.append(int(item))

    data.append(start_line)

    index = 0

    while True:
        values_list = get_differences(data[index])
        data.append(values_list)

        zero_test = test_differences(values_list)
        if zero_test:
            break

        index += 1

    # print_data(data)
    data = calculate(data)
    # print_data(data)

    return data[0][-1]


def part1(debug=True):
    lines = get_data(debug)

    result = 0

    for line in lines:
        result += process_line(line)

    print(result)


def part2(debug=True):
    lines = get_data(debug)


if __name__ == "__main__":
    part1(False)
    part2()
