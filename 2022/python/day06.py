from common import get_file_contents


def process_data(letter_list):
    temp_data = []

    for index, letter in enumerate(letter_list):
        if len(temp_data) < 4:
            temp_data.append(letter)
            continue

        if len(set(temp_data)) == 4:
            return index

        temp_data.append(letter)
        temp_data.pop(0)

def test_p1():
    test_letters = [
        (list("mjqjpqmgbljsphdztnvjfqwrcgsmlb"), 7),
        (list("bvwbjplbgvbhsrlpgdmjqwftvncz"), 5),
        (list("nppdvjthqldpwncqszvftbrmjlhg"), 6),
        (list("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 10),
        (list("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 11)
    ]

    for test_list, expected_val in test_letters:
        result = process_data(test_list)
        assert result == expected_val

    print("Finished Tests")


def p1():
    lines = get_file_contents("data/day06_input.txt")
    letters = list(lines[0])

    result = process_data(letters)
    print(result)

def p2():
    pass


def main():
    p1()


if __name__ == "__main__":
    main()
