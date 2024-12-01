import os
import common
import collections



def check_counts(data):
    has_two = False
    has_three = False

    for k, v in data.items():
        if v == 2 and has_two is False:
            has_two = True
        if v == 3 and has_three is False:
            has_three = True
    return (has_two, has_three)


def part1():
    real_file = os.path.join("..", "data", "day02_input.txt")
    data = common.get_file_contents(real_file)

    two = 0
    three = 0

    for line in data:
        parts = list(line)
        count = collections.defaultdict(int)
        for letter in parts:
            count[letter] += 1
        has_two, has_three = check_counts(count)
        if has_two:
            two += 1
        if has_three:
            three += 1
    return two * three


def diff_lists(item1, item2):
    diff_number = 0

    list1 = list(item1)
    list2 = list(item2)

    for index, letter in enumerate(list1):
        if list2[index] != letter:
            diff_number += 1

    return diff_number


def part2():
    real_file = os.path.join("..", "data", "day02_input.txt")
    data = common.get_file_contents(real_file)

    answers = []

    # get the two lines that only differ by one letter
    for item1 in data:
        for item2 in data:
           if item1 == item2:
               continue
           if diff_lists(item1, item2) == 1:
              answers.append(item1)
              answers.append(item2)
              break
        if len(answers) == 2:
            break

    # figure out the common letters
    answer = ""
    for index, letter in enumerate(answers[0]):
        if letter == answers[1][index]:
            answer += letter
    return answer


def main():
    answer_part1 = part1()
    answer_part2 = part2()

    print("Part 1", answer_part1)
    print("Part 2", answer_part2)


if __name__ == "__main__":
    main()
