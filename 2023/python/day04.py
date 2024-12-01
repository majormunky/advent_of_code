import common


test_data = [
	"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
	"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
	"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
	"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
	"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
	"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]


def split_numbers(line):
	parts = line.split(" ")
	result = []
	for part in parts:
		num = part.strip()
		if num:
			result.append(num)
	return result


def parse_card(line):
	parts = line.split("|")
	winning_numbers = split_numbers(parts[0].split(":")[-1])
	card_num = parts[0].split(":")[0]
	card_numbers = split_numbers(parts[-1])

	return {
		"card": card_num,
		"winning_numbers": set(winning_numbers),
		"card_numbers": set(card_numbers)
	}


def get_winning_numbers(card):
	return len(card["card_numbers"] & card["winning_numbers"])


def get_card_score(amount_matched):
	if amount_matched == 0:
		return 0

	score = 1
	doubling_times = amount_matched - 1

	for i in range(doubling_times):
		score *= 2

	return score


def part1(debug=True):
	if debug:
		data = test_data
	else:
		data = common.get_file_contents("../data/day04_input.txt")

	answer = 0
	for line in data:
		card = parse_card(line)
		matched = get_winning_numbers(card)
		card_score = get_card_score(matched)
		answer += card_score

	print(answer)


def get_card_number(card):
	parts = card["card"].split(" ")
	return int(parts[-1])


def get_winning_cards(card_num, amount):
	result = []

	for i in range(amount):
		result.append(card_num + i + 1)

	return result


def part2(debug=True):
	if debug:
		data = test_data
	else:
		data = common.get_file_contents("../data/day04_input.txt")

	win_data = {}
	cards = []

	for line in data:
		card = parse_card(line)
		card_number = get_card_number(card)
		matched = get_winning_numbers(card)
		winning_cards = get_winning_cards(card_number, matched)
		win_data[card_number] = winning_cards

		cards.extend(winning_cards)

		existing_cards = cards.count(card_number)

		for i in range(existing_cards):
			cards.extend(win_data[card_number])

		cards.append(card_number)

	# print(sorted(cards))
	print(len(cards))


if __name__ == '__main__':
	part1(False)
	part2(False)
