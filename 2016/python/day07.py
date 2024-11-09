import sys
import common


def get_filename():
    filename = sys.argv[0]
    filename = filename.split("/")[-1]
    filename = filename.split(".")[0]
    return filename

data = common.get_file_contents("data/{}_input.txt".format(get_filename()))


def get_text_between_delimiters(val, delimiters):
    result = []

    # aaa[bbb]aaa[ccc]ddd
    od, cd = delimiters
    parts = val.split(od)

    for part in parts[1:]:
        sub_part = part.split(cd)
        result.append(sub_part[0])

    return result


def convert_aba_to_bab(val):
    return f"{val[1]}{val[0]}{val[1]}"


def check_for_bab(val, aba_strings):
    # print("Check for bab", val, aba_strings)
    if len(aba_strings) == 0:
        return False

    inner_strings = get_text_between_delimiters(val, ["[", "]"])

    for i in inner_strings:
        for aba_string in aba_strings:
            bab_string = convert_aba_to_bab(aba_string)
            # print(f"Converting aba ({aba_string}) string to bab format ({bab_string})")
            # print(f"Does {bab_string} show up in {i}")
            if bab_string in i:
                # print("True")
                return True
            # else:
            #     print("False")
    return False


def check_for_aba(val):
    val_len = len(val)
    inside_brackets = False
    aba_strings = []

    for i in range(val_len - 2):
        cur = val[i]

        if cur == "[":
            inside_brackets = True
        elif cur == "]":
            inside_brackets = False

        check_char = val[i + 2]

        if cur == check_char:
            if not inside_brackets:
                aba_strings.append(f"{cur}{val[i + 1]}{check_char}")
    return check_for_bab(val, aba_strings)

def check_for_abba(val):
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
        if check_for_abba(line):
            result += 1

    return result


def part2():
    result = 0
    for line in data:
        if check_for_aba(line):
            result += 1
    return result


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
