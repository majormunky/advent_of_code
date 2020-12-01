import common
import collections


data = common.get_file_contents("data/day4_input.txt")


def get_most_common(data):
    result = {}
    for item in data:
        key = str(item[1])
        if key not in result.keys():
            result[key] = []
        result[key].append(item[0])
        if len(result[key]) > 1:
            result[key] = sorted(result[key])
    answer = []
    for k, v in result.items():
        for av in v:
            answer.append(av)
    return "".join(answer[:5])


def get_checksum(line):
    # vxupkizork-sgmtkzoi-pkrrehkgt-zxgototm-644[kotgr]
    parts = line.split("-")

    # This will get us ["644", "kotgr]"]
    checksum_parts = parts.pop().split("[")

    # to get our checksum, we need to get rid of the last bracket
    checksum = checksum_parts[1].replace("]", "")

    # the sector id we can just convert to an int
    sector_id = int(checksum_parts[0])

    return (sector_id, checksum)


def check_password(line):
    # vxupkizork-sgmtkzoi-pkrrehkgt-zxgototm-644[kotgr]
    parts = line.split("-")

    # to get our checksum, we need to get rid of the last bracket
    sector_id, checksum = get_checksum(line)

    # our list of letters
    letters = []

    # go over each letter in our password
    for character in "".join(parts):
        letters.append(character)

    counter = collections.Counter(letters)

    # some of the most common will have the same amount
    # so we need to be sure we grab the results sorted alphabetically
    checksum_result = get_most_common(counter.most_common(15))

    # if our checksum matches, we can return the sector id
    if checksum_result == checksum:
        return sector_id
    else:
        # if not, just return 0
        return 0

def part1():
    answer = 0
    for line in data:
        answer += check_password(line)
    return answer


def part2():
    return "not complete"


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
