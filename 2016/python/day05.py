import os
import common
import hashlib


def get_md5(val):
    result = hashlib.md5(val.encode())
    return result.hexdigest()

def part1():
    real_file = os.path.join("..", "data", "day05_input.txt")
    data = common.get_file_contents(real_file, single_line=True)

    # counter to be used in our test string
    i = 0

    # our answer
    answer = ""

    # loop until our answer is 8 characters long
    while len(answer) < 8:
        # our string to test
        test_string = "{}{}".format(data, i)

        # md5 hash of test string
        hash_val = get_md5(test_string)

        # check if its special
        if hash_val.startswith("00000"):
            # it is, grab the 6th character and add it to our answer
            answer += str(hash_val[5])

        # sanity check
        if i > 5_000_000_000:
            print("Broke 5 Billion, Stopping")
            print(answer)
            break

        # increment counter
        i += 1
    return answer


def part2():
    real_file = os.path.join("..", "data", "day05_input.txt")
    data = common.get_file_contents(real_file, single_line=True)

    i = 0
    answer = [None, None, None, None, None, None, None, None]
    done = False
    while not done:
        i += 1
        test_string = "{}{}".format(data, i)
        hash_val = get_md5(test_string)
        if hash_val.startswith("00000"):
            try:
                index = int(hash_val[5])
                val = hash_val[6]
                if answer[index] is None:
                    answer[index] = val
                    print(i, print_answer(answer))
                if all(answer):
                    done = True
            except (ValueError, IndexError):
                continue

        if i > 5_000_000_000:
            print(answer)
            print("Stopping at 5 billion")
            break

    return "".join(answer)

def print_answer(letters):
    result = ""
    for character in letters:
        if character is None:
            result += "_"
        else:
            result += character
    return result

def main():
    part1_answer = part1()
    part2_answer = part2()

    # not 76301cc0

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
