import common
import collections
import functools


test_lines = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]

CARD_VALUES = [
    "A",
    "K",
    "Q",
    "J",
    "T",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
]


SCORES = {
    "five-of-a-kind": 1,
    "four-of-a-kind": 2,
    "full-house": 3,
    "three-of-a-kind": 4,
    "two-pair": 5,
    "one-pair": 6,
    "high-card": 7,
}


def card_compare(x, y):
    x_hand = x["hand"]
    y_hand = y["hand"]
    for index in range(len(x_hand)):
        x_char = x_hand[index]
        y_char = y_hand[index]
        x_val = CARD_VALUES.index(x_char)
        y_val = CARD_VALUES.index(y_char)

        if x_val < y_val:
            return -1
        elif y_val < x_val:
            return 1

    return 0


def score_hand(cards, bet):
    set_length = len(set(cards))

    key = None

    if set_length == 1:
        key = "five-of-a-kind"

    elif set_length == 2:
        for char in cards:
            char_count = cards.count(char)
            if char_count == 4:
                key = "four-of-a-kind"
        if key is None:
            key = "full-house"

    elif set_length == 3:
        # could be three of a kind or two pair
        for char in cards:
            char_count = cards.count(char)
            if char_count == 3:
                key = "three-of-a-kind"
            elif char_count == 2:
                key = "two-pair"

    elif set_length == 4:
        key = "one-pair"
    else:
        key = "high-card"

    return {"name": key, "value": SCORES[key], "hand": cards, "bet": bet}


def parse_lines(lines):
    result = []
    for line in lines:
        result.append(line.split(" "))
    return result


def part1(debug=True):
    if debug:
        lines = test_lines
    else:
        lines = common.get_file_contents("data/day07_input.txt")

    data = parse_lines(lines)

    scores = collections.defaultdict(list)

    # build dictionary of hands and what type of win they are
    for item in data:
        hand, bet = item
        score = score_hand(hand, bet)
        scores[score["name"]].append(score)

    sorted_hands = []

    # sort the dictionary hands into flat list with best at the start
    for key in SCORES.keys():
        if len(scores[key]) == 1:
            sorted_hands.append(scores[key][0])
        else:
            sorted_by_hand_type = sorted(
                scores[key], key=functools.cmp_to_key(card_compare)
            )
            sorted_hands.extend(sorted_by_hand_type)

    answer = 0

    multiplier = 1

    # start our list with the worst hand first
    for item in reversed(sorted_hands):
        answer += int(item["bet"]) * multiplier
        multiplier += 1

    print(answer)


if __name__ == "__main__":
    part1(False)
