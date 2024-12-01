import sys
import common
import functools

test_data = [
    "???.### 1,1,3",
    ".??..??...?##. 1,1,3",
    "?#?#?#?#?#?#?#? 1,3,1,6",
    "????.#...#... 4,1,1",
    "????.######..#####. 1,6,5",
    "?###???????? 3,2,1",
]


def get_data(debug, data):
    if debug:
        data = list(data)
    else:
        data = common.get_file_contents("../data/day12_input.txt")
    return data


def generate_spring_configurations(springs):
    print(f"Running gsc with {len(springs)} springs")
    for spring in springs:
        spring_list = list(spring)
        for char_index, char in enumerate(spring_list):
            if char == "?":
                test_1 = list(spring)
                test_2 = list(spring)

                test_1[char_index] = "#"
                test_2[char_index] = "."

                test_1_string = "".join(test_1)
                test_2_string = "".join(test_2)

                # print(test_1_string, test_2_string)

                # springs.extend(generate_spring_configurations([test_1_string]))
                # springs.extend(generate_spring_configurations([test_2_string]))

                springs.extend(
                    generate_spring_configurations([test_1_string, test_2_string])
                )

                return springs

    return springs


def non_rec_gsd(spring_list):
    print("Running with ", spring_list)
    result = []

    while True:
        print("At top of while loop")
        if len(spring_list) == 0:
            print("Spring list is empty, breaking")
            break

        first = spring_list.pop(0)
        print(f"Spring list is now {len(spring_list)}")
        print(f"Result is now {len(result)}")
        print(result)
        item = list(first)
        for index, char in enumerate(item):
            if char == "?":
                left = item.copy()
                right = item.copy()

                left[index] = "#"
                right[index] = "."

                spring_list.append("".join(left))
                spring_list.append("".join(right))
                print("Breaking")
                break
        result.append(first)
    return result


def gsd(spring_list, result):
    print(f"Spring List Length: {len(spring_list)}")
    # print(spring_list)
    if len(spring_list) == 0:
        return result
    else:
        while True:
            next_spring = spring_list.pop()
            # print(f" Spring List Length: {len(spring_list)}")
            item = list(next_spring)
            # print(f" Checking {next_spring}")
            # print()
            for index, char in enumerate(item):
                if char == "?":
                    left = item.copy()
                    right = item.copy()

                    left[index] = "#"
                    right[index] = "."

                    spring_list.append("".join(left))
                    spring_list.append("".join(right))

                    return gsd(spring_list, result)
            # print("Next spring is ? free, adding to result", next_spring)
            result.append(next_spring)

    print("returning result")
    return result


def r(item_list, result):
    if not item_list:
        return result
    # remove first item from list
    # print(item_list)
    item = item_list.pop(0)

    item_split = list(item)

    for char_index, char in enumerate(list(item_split)):
        if char == "?":
            item_left = item_split.copy()
            item_right = item_split.copy()

            item_left[char_index] = "#"
            item_right[char_index] = "."

            item_list.extend(["".join(item_left), "".join(item_right)])

            return r(item_list, result)

    result.append(item)
    return r(item_list, result)


def split_line(line):
    data = line.split(" ")

    counts = []
    for count in data[1].split(","):
        counts.append(int(count))

    springs = data[0]

    return springs, counts


def process_line(line):
    springs, counts = split_line(line)

    options = generate_spring_configurations([springs])

    test_springs = []

    for option in options:
        if "?" not in option and is_valid_data(option, counts):
            test_springs.append(option)

    return len(test_springs)


def process_line_part_2(line):
    spring, count = split_line(line)
    spring, count = expand_line(spring, count)
    return check_springs(spring, count)


def is_valid_data(springs, spring_data):
    temp_parts = springs.split(".")
    parts = []

    for p in temp_parts:
        if p != "":
            parts.append(p)

    if len(parts) != len(spring_data):
        return False

    for index, amount in enumerate(spring_data):
        if len(parts[index]) != amount:
            return False

    return True


def expand_line(springs, count):
    spring_list = [springs] * 5
    expanded_spring = "?".join(spring_list)
    count_list = count * 5

    return expanded_spring, count_list


def part1(debug=True):
    lines = get_data(debug, test_data)
    # process_line(lines[1])
    result = 0
    for line in lines:
        result += process_line(line)
    print(result)


cache = {}


def check_springs(val, groups, depth=0):
    enable_print = True

    extra_spaces = " " * depth

    val_key = f"{val}-{str(groups)}"
    if val_key in cache:
        if enable_print:
            print(f"{extra_spaces}Val {val_key} in cache, returning {cache[val_key]}")
        return cache[val_key]

    if enable_print:
        print()
        print(f"{extra_spaces}{''.join(val)} {groups}")
    result = 0
    if len(val) == 0 and len(groups) == 0:
        if enable_print:
            print(f"{extra_spaces}Returning 1 because val and group is empty")
        cache[val_key] = 1
        return 1

    if len(val) == 0 and len(groups) > 0:
        if enable_print:
            print(f"{extra_spaces}Returning 0 because we have groups left")
        cache[val_key] = 0
        return 0

    if len(val) and len(groups) == 0:
        if enable_print:
            print(f"{extra_spaces}Returning 1 because we ran out of groups")
        cache[val_key] = 1
        return 1

    if len(val) < len(groups):
        if enable_print:
            print(f"{extra_spaces}Returning 0 because we have more groups than springs")
        cache[val_key] = 0
        return 0

    if len(val) == len(groups) and len(groups) == 1:
        if groups[0] > 1:
            if enable_print:
                print(f"{extra_spaces}Returing 0 because our final group is too big")
            cache[val_key] = 0
            return 0

    if len(val) < groups[0]:
        cache[val_key] = 0
        return 0

    val_list = list(val)
    if val_list[0] == ".":
        if enable_print:
            print(f"{extra_spaces}First char is a . - removing it")
        val_list.pop(0)

        if enable_print:
            print(f"{extra_spaces}Value is now: {''.join(val_list)}")
        result += check_springs("".join(val_list), groups.copy(), depth + 1)
    elif val[0] == "?":
        if enable_print:
            print(f"{extra_spaces}First char is a ?")
        val_1 = val_list
        val_2 = val_list.copy()
        val_1[0] = "#"
        val_2[0] = "."
        result += check_springs("".join(val_1), groups.copy(), depth + 1)
        result += check_springs("".join(val_2), groups.copy(), depth + 1)
    else:
        if enable_print:
            print(f"{extra_spaces}First char is a #")
        # string starts with a #
        works = True

        # check to see if we have enough # in a row to
        # match up with the group we are on

        # loop through the amount of items that equals the group length
        for i in range(groups[0]):
            # if any of these characters within the group
            # are a period, it means the group ended
            # and our group amount can't fit here
            if val[i] == ".":
                if enable_print:
                    print(f"{extra_spaces}Found . when checking spring group")
                works = False
                break

        if works is False:
            # print("Returning 0 because we have a # but not long enough for our group")
            cache[val_key] = 0
            return 0
        else:
            # remove the amount of characters we matched with
            if enable_print:
                print(
                    f"{extra_spaces}Removing {groups[0]} characters from string that were matched"
                )
            for i in range(groups[0]):
                val_list.pop(0)

            if enable_print:
                print(f"{extra_spaces}String is now {''.join(val_list)}")

            if len(val_list) > 0:
                # check to be sure our next character isn't a #
                # otherwise our group number needs to be higher to match
                if val_list[0] == "#":
                    if enable_print:
                        print(
                            f"{extra_spaces}After removing matched springs, our next spring is also a #, returning 0"
                        )
                    cache[val_key] = 0
                    return 0

                # if the next character is a ?, it has to be a .
                if val_list[0] == "?":
                    if enable_print:
                        print(
                            f"{extra_spaces}After removing matched strings, the next spring is a ?, setting to ."
                        )
                    val_list[0] = "."

            if enable_print:
                print(f"{extra_spaces}Removing group item")
            groups.pop(0)
            if enable_print:
                print(f"{extra_spaces}Group is now {str(groups)}")
            result += check_springs("".join(val_list), groups.copy(), depth + 1)
    if enable_print:
        print(f"{extra_spaces}Returning result: {result} from val {val}")
    cache[val_key] = result
    return result


def part2(debug=True):
    global cache
    # sys.setrecursionlimit(100000000)
    lines = get_data(debug, test_data)

    result = 0

    for line in lines:
        # cache = {}
        count = process_line_part_2(line)
        result += count
        print(f"{count}: {line}")

    print(result)


def individual_test(line):
    count = process_line_part_2(line)
    print(count, line)


if __name__ == "__main__":
    # part1(False) # 7916

    # 37399963866042 too high
    # 1061322386 too low
    # part2(True)
    individual_test("????.#...#... 4,1,1")
