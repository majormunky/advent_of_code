import common
import string
import json


test_data = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


def get_part_numbers_from_line(line, row_index):
    """
    Takes a line in and returns a list of dictionaries
    Each dictionary describes the position and length
    of the part number within the line
    """
    width = len(line)

    result = []
    temp_word = {}
    start_word = False

    # go character by character
    for col_index in range(width):
        # check if the character is a period
        if line[col_index] == ".":
            # if so, we now need to know if we were building a part number
            # if start_word is true, we need to "close off" that number
            if start_word:
                # add our part number to the result
                result.append(temp_word)

                # reset our start_word flag
                start_word = False

                # reset the data dict we are building
                temp_word = {}
        # otherwise, is the next character a digit
        elif line[col_index] in string.digits:
            # if so, we are either starting a new part number, or continuing one
            # if start_word is false, it means we are starting one
            if start_word is False:
                # record some data about its position
                temp_word["row"] = row_index
                temp_word["col"] = col_index
                temp_word["length"] = 1
                temp_word["word"] = line[col_index]

                # and set our flag indicating we are building a part number
                start_word = True
            else:
                # if start_word is true, and our character is a digit
                # it means we are in the middle of building a part number
                temp_word["length"] += 1
                temp_word["word"] += line[col_index]
        # if the above fail, it means we have a symbol
        else:
            # and in that case, the only thing we need to check
            # is if we were building a part number
            if start_word:
                # if so, its the end of the part number, close it off
                result.append(temp_word)
                start_word = False
                temp_word = {}

    # if our part number is the last digits in the line, we will still have
    # a part number, be sure to add it
    if temp_word:
        result.append(temp_word)

    return result


def get_part_numbers(data):
    height = len(data)

    part_numbers = []

    for row_index in range(height):
        part_numbers.extend(get_part_numbers_from_line(data[row_index], row_index))

    return part_numbers


def is_valid_part_number(part_data, data):
    """
    This takes in a dictionary describing a part number
    and checks if there is any punctuation next to it
    if so, it means its a valid part
    """
    part_identifiers = string.punctuation
    part_identifiers = part_identifiers.replace(".", "")

    # build row indexes for above and below the current line
    above_row_index = part_data["row"] - 1
    below_row_index = part_data["row"] + 1

    # do the same thing, but horizontally
    col_range = range(
        max(part_data["col"] - 1, 0),
        min(part_data["col"] + part_data["length"] + 1, len(data[0])),
    )

    # first check if we have any symbols directly to the left
    if data[part_data["row"]][col_range[0]] in part_identifiers:
        return True

    # or right of our part number
    if data[part_data["row"]][col_range[-1]] in part_identifiers:
        return True

    # otherwise check the row above
    if above_row_index >= 0:
        for col_index in col_range:
            text_check = data[above_row_index][col_index]
            if text_check in part_identifiers:
                return True

    # and then the row below
    if below_row_index < len(data):
        for col_index in col_range:
            text_check = data[below_row_index][col_index]
            if text_check in part_identifiers:
                return True

    # if all of our checks fail, it isn't a valid part number
    return False


def part1(debug=False):
    if debug:
        data = test_data
    else:
        data = common.get_file_contents("../data/day03_input.txt")

    part_numbers = get_part_numbers(data)
    valid = []
    answer = 0

    for pn in part_numbers:
        if is_valid_part_number(pn, data):
            valid.append(pn)
            answer += int(pn["word"])

    print(answer)


def output_html(data):
    output = "<html>\n"
    output += "<head>\n"
    output += "</head>\n"
    output += "<body>\n"
    output += "<table>\n"

    for line_index, line in enumerate(data):
        output += "<tr>\n"
        for char_index, char in enumerate(line):
            output += f"<td data-cell-id='{line_index}_{char_index}'>{char}</td>\n"
        output += "</tr>\n"

    output += "</table>\n"
    output += "</body>\n"
    output += "</html>\n"

    with open("test.html", "w") as f:
        f.write(output)


def get_gear_positions(data):
    result = []

    width = len(data[0])
    height = len(data)

    for row in range(height):
        for col in range(width):
            if data[row][col] == "*":
                result.append([row, col])
    return result


def check_for_valid_gear(gear, data):
    # build list of places to check for gear ratios
    # this will be the 8 surrounding spots of the gear
    cells_to_check = [
        [gear[0] - 1, gear[1] - 1],
        [gear[0] - 1, gear[1]],
        [gear[0] - 1, gear[1] + 1],
        [gear[0], gear[1] - 1],
        [gear[0], gear[1] + 1],
        [gear[0] + 1, gear[1] - 1],
        [gear[0] + 1, gear[1]],
        [gear[0] + 1, gear[1] + 1],
    ]

    nums_found = []

    for cell in cells_to_check:
        try:
            if data[cell[0]][cell[1]] in string.digits:
                nums_found.append(cell)
        except IndexError:
            pass

    return nums_found


def get_start_position_of_gear_ratio(row, col, data):
    # given a row and column of one of the characters in our gear ratio
    # find the position of the first character for it
    starting_pos = col - 1

    while True:
        try:
            if data[row][starting_pos] in string.digits:
                starting_pos -= 1
            else:
                starting_pos += 1
                break
        except IndexError:
            break

    return [row, starting_pos]


def get_gear_ratio(row, col, data):
    # given a row and column, return the full gear ratio number
    result = ""

    # we aren't sure how long this gear ratio will be
    # so we use a while loop
    while True:
        # we may try a position out of the 'board', if so
        # it means we reached the end
        try:
            if data[row][col] in string.digits:
                result += data[row][col]
                col += 1
            else:
                break
        except IndexError:
            break
    return result


def get_gear_ratios(gear_list, data):
    # use a set in case we have two gear positions within the same number
    result = set()

    # go over each gear ratio position
    for gear in gear_list:
        # find the starting character position for this ratio
        start_pos_for_gear = get_start_position_of_gear_ratio(gear[0], gear[1], data)

        # using the starting position, return the full gear ratio number
        gear_ratio = get_gear_ratio(start_pos_for_gear[0], start_pos_for_gear[1], data)

        # add it to our set
        result.add(int(gear_ratio))

    return list(result)


def part2(debug=False):
    if debug:
        data = test_data
    else:
        data = common.get_file_contents("../data/day03_input.txt")
    answer = 0

    # first, get a list of row / col indexes that contain a *
    gears = get_gear_positions(data)

    for gear in gears:
        # next, get a list of row / col index that suround the *
        gear_ratio_list = check_for_valid_gear(gear, data)

        # using those row / col indexes, return the full number
        # our current position may be any character within the
        # gear ratio, so we need to be sure we get the full
        # number back
        gear_ratios = get_gear_ratios(gear_ratio_list, data)

        # our only valid gear ratios will have two numbers
        if len(gear_ratios) == 2:
            # if so, multiply them together to get our answer
            answer += gear_ratios[0] * gear_ratios[1]

    print(answer)


if __name__ == "__main__":
    part1()
    part2()
