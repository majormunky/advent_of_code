import common
import collections


test_lines = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


def part1_boxcheck(box_dict):
    # 12 red cubes, 13 green cubes, and 14 blue
    if "red" in box_dict.keys() and box_dict["red"] > 12:
        return False

    if "green" in box_dict.keys() and box_dict["green"] > 13:
        return False

    if "blue" in box_dict.keys() and box_dict["blue"] > 14:
        return False

    return True


def get_box_data(lines):
    result = collections.defaultdict(list)

    for line in lines:
        # split our game id and the list of box data
        game_id, box_data = line.split(":")
        game_key = game_id.split(" ")[-1]

        # split the box data into the groups the elves show us
        box_sets = box_data.split(";")

        # go over each box group, this is what the elf is showing us
        for box_set in box_sets:
            box_list = []
            for box_item in box_set.strip().split(","):
                box_list.append(box_item.strip())
            result[game_key].append(box_list)

    return result


def part1():
    lines = common.get_file_contents("data/day02_input.txt")

    good_games = []

    box_data = get_box_data(lines)

    for box_id, box_list in box_data.items():
        box_status = []
        for box_set in box_list:
            box_dict = {"red": 0, "green": 0, "blue": 0}
            for box_item in box_set:
                box_amount, box_color = box_item.split(" ")
                box_dict[box_color] += int(box_amount)

            box_status.append(part1_boxcheck(box_dict))
        if all(box_status):
            good_games.append(int(box_id))

    print(sum(good_games))


def part2():
    lines = get_box_data(test_lines)
    print(lines)


if __name__ == "__main__":
    part1()  # 2006
    # part2()
