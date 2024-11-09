import sys
import common


def get_filename():
    filename = sys.argv[0]
    filename = filename.split("/")[-1]
    filename = filename.split(".")[0]
    return filename

data = common.get_file_contents("data/{}_input.txt".format(get_filename()))


def check_for_abba(val):
    current_index = 0
    val_len = len(val)
    inside_brackets = False
    has_abba_in_brackets = False
    has_abba = False

    for i in range(val_len - 3):
        current_char = val[i]
        if current_char == "[":
            inside_brackets = True
        elif current_char == "]":
            inside_brackets = False
        else:
            next_char = val[i + 1]
            first_check = val[i + 2]
            second_check = val[i + 3]

            check_list = [current_char, next_char, first_check, second_check]

            if next_char == first_check and current_char == second_check:
                diff_chars_check = set(check_list)
                diff_len = len(diff_chars_check)
                if diff_len == 1:
                    continue

                if inside_brackets:
                    has_abba_in_brackets = True
                else:
                    has_abba = True

    if has_abba_in_brackets:
        return False
    return has_abba


test_ips = {
    "abba[mnop]qrst": True,
    "abcd[bddb]xyyx": False,
    "aaaa[qwer]tyui": False,
    "ioxxoj[asdfgh]zxcvbn": True,
    "omrmyxygfmlnlpd[mvszaozmwrfqpup]zqdogulmykihlubuv[xdmdckgkvqmnetqlab]xmpghceghczgavrrv": True
}


def test_ip_values():
    k = "omrmyxygfmlnlpd[mvszaozmwrfqpup]zqdogulmykihlubuv[xdmdckgkvqmnetqlab]xmpghceghczgavrrv"
    v = True
    # for k, v in test_ips.items():
    result = check_for_abba(k)
    assert v == result


def part1():
    result = 0
    for line in data:
        line_res = check_for_abba(line)
        if line_res:
            result += 1

    return result


def part2():
    return "not complete"


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
    # test_ip_values()
