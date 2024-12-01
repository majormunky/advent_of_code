import os
import common
from collections import defaultdict


def p1():
    real_file = os.path.join("..", "data", "day08_input.txt")
    lines = common.get_file_contents(real_file)

    # the digits dict represents a mapping between how many segments are active
    # and the actual value that is supposed to be reprenenting
    digits = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }
    found = 0

    for line in lines:
        parts = line.split("|")
        more_parts = parts[1].split(" ")
        for item in more_parts:
            if len(item) in digits.keys():
                found += 1
    return found


def calculate_digits(digit_list):
	digit_to_segments = {}
	length_to_item = defaultdict(list)

	# first we setup our known digits
	# as well as create a dictionary for easily getting all of the digits with a certain segment length
	for item in digit_list:
		if len(item) == 2:
			# this is the 1 character
			# we may not know which is the one that is at the top
			digit_to_segments[1] = set(list(item))

		if len(item) == 3:
			digit_to_segments[7] = set(list(item))
			# this is the 7 character

		if len(item) == 4:
			digit_to_segments[4] = set(list(item))

		if len(item) == 7:
			digit_to_segments[8] = set(list(item))

		length_to_item[len(item)].append(item)


	# now that we have some info, lets now work with 6, 9 and 0
	six_or_nine = list(length_to_item[6])

	# we should now have 3 items in this list, the 6, 9 and 0 digits
	# the 6 isn't going to have all the segments that a 1 has, so we can start there
	# upper_right_segment = None
	for i in six_or_nine:
		letter_list = set(i)
		diff = letter_list - digit_to_segments[1]
		if len(diff) == 5:
			# this is a 6
			digit_to_segments[6] = set(list(i))
			# upper_right_segment = digit_to_segments[1] - letter_list
			six_or_nine.remove(i)

	# we now have 6 set
	# six_or_nine now contains the 9 and 0
	# pause on these for a moment

	# we need to now deal with digits with 5 segments
	# this includes 2, 3, and 5
	# whichever one of these 3 items that has both the 1 segments is the 3
	two_three_or_5 = list(length_to_item[5])

	for item in two_three_or_5:
		item_set = set(list(item))
		diff = digit_to_segments[1] - item_set
		if len(diff) == 0:
			# we found the three
			digit_to_segments[3] = item_set
			two_three_or_5.remove(item)
			break

	# now we can figure out the 6 and 9 now that we have the 3 segments
	for sn in six_or_nine:
		sn_set = set(list(sn))
		diff = sn_set - digit_to_segments[3]
		if len(diff) == 1:
			# this is a 9
			digit_to_segments[9] = sn_set
		else:
			# this is a 0
			digit_to_segments[0] = sn_set

	# and now that we have the 9 set, we can figure out the 5 and 2
	for item in two_three_or_5:
		item_set = set(list(item))
		diff = digit_to_segments[9] - item_set
		if len(diff) == 1:
			# this is a 5
			digit_to_segments[5] = item_set
		else:
			# this is a 2
			digit_to_segments[2] = item_set

	return digit_to_segments



def p2():
    real_file = os.path.join("..", "data", "day08_input.txt")
    lines = common.get_file_contents(real_file)

    # segment count -> digit
    result = 0

    # figure out what the other digits are
    for line in lines:
        parts = line.split("|")
        all_digits = parts[0].split(" ")
        value_parts = parts[1].split(" ")
        digit_mapping = calculate_digits(all_digits)
        value = []

        for vp in value_parts:
            vp_set = set(list(vp))
            for digit, letter_set in digit_mapping.items():
                if len(vp_set.symmetric_difference(letter_set)) == 0:
                    value.append(str(digit))

        int_val = int("".join(value))
        result += int_val
    return result

if __name__ == '__main__':
	print("Part 1:", p1())
	print("Part 2:", p2())
