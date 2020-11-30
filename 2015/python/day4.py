import hashlib


puzzle_input = "ckczppom"


def get_md5(val):
	result = hashlib.md5(val.encode())
	return result.hexdigest()


def part1():
	i = 0
	while True:
		test_val = get_md5("{}{}".format(puzzle_input, i))
		if test_val.startswith("000000"):
			print(i)
			break

		i += 1

		if i > 10_000_000:
			print("Broke 3 million, stopping")
			break


def main():
	part1()


if __name__ == '__main__':
	main()