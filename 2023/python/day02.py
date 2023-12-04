import common
import collections


def part1_boxcheck(box_dict):
    # 12 red cubes, 13 green cubes, and 14 blue
    if "red" in box_dict.keys() and box_dict["red"] > 12:
        print("Too many red")
        return False

    if "green" in box_dict.keys() and box_dict["green"] > 13:
        print("Too many green")
        return False

    if "blue" in box_dict.keys() and box_dict["blue"] > 14:
        print("Too many blue")
        return False

    return True


def part1():
    test_lines = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]

    lines = common.get_file_contents("data/day02_input.txt")

    good_games = []

    for line in lines:
        # split our game id and the list of box data
        game_id, box_data = line.split(":")

        # split the box data into the groups the elves show us
        box_sets = box_data.split(";")

        # Need to keep track if all the box groups pass the test
        box_status = []

        # go over each box group, this is what the elf is showing us
        for box_set in box_sets:
            # used to keep track of how many boxes we have
            boxes = collections.defaultdict(int)

            # break up our box set into individual box amounts / colors
            for box in box_set.split(","):
                # separate the box amount and color
                box_amount, box_color = box.strip().split(" ")

                # track how many boxes of that color we have
                boxes[box_color] += int(box_amount)

            # add to our box status list the result of our test
            # if true, it means the box check passed
            box_status.append(part1_boxcheck(boxes))

        # if all the tests pass for a game, its valid
        if all(box_status):
            print(f"{game_id} Passed")
            _, game_num = game_id.split(" ")
            good_games.append(int(game_num))
        else:
            print(f"{game_id} Failed")
        print("")

    # print out the sum of all the valid games
    print(good_games)
    print(sum(good_games))


def part2():
    pass


if __name__ == "__main__":
    part1()  # 2006
    part2()
