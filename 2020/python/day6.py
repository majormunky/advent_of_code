import sys
import common


def get_filename():
    filename = sys.argv[0]
    filename = filename.split("/")[-1]
    filename = filename.split(".")[0]
    return filename


data = common.get_file_contents("data/{}_input.txt".format(get_filename()))


def split_into_groups(lines):
    """
    For this to work i had to add an extra blank
    line at the end of the data file
    """
    groups = []
    group = []
    for line in lines:
        if len(line) == 0 and len(group):
            groups.append(group)
            group = []
            continue
        group.append(line)
    return groups


def count_answers(answer_list):
    answers = set()
    for answer in answer_list:
        for char in answer:
            answers.add(char)
    return len(answers)


def count_all_answers(answer_list):
    people_count = len(answer_list)
    data = {}
    result = 0
    for answer in answer_list:
        for char in answer:
            if char not in data.keys():
                data[char] = 0
            data[char] += 1
    for k, v in data.items():
        if v == people_count:
            result += 1
    return result



def part1():
    total = 0
    groups = split_into_groups(data)
    for g in groups:
        total += count_answers(g)
    return total


def part2():
    total = 0
    groups = split_into_groups(data)
    for g in groups:
        total += count_all_answers(g)
    return total
    

def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
