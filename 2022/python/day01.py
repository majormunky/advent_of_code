import os
import common


def get_calorie_count(items):
    return sum(items)


def get_data():
    filepath = os.path.join("..", "data", "day01_input.txt")
    lines = common.get_file_contents(filepath)

    elves = []

    new_group = []
    for line in lines:
        if line == "":
            elves.append(new_group)
            new_group = []
        else:
            new_group.append(int(line))
    return elves


def p1():
    elves = get_data()

    most_calories = 0

    for elf in elves:
        count = get_calorie_count(elf)
        if count > most_calories:
            most_calories = count

    print(most_calories)


def p2():
    elves = get_data()
    counts = []

    for elf in elves:
        counts.append(get_calorie_count(elf))

    counts = sorted(counts)

    total = counts[-1] + counts[-2] + counts[-3]
    print(total)


if __name__ == "__main__":
    p1()
    p2()
