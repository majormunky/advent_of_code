import sys
import common


def get_filename():
    filename = sys.argv[0]
    filename = filename.split("/")[-1]
    filename = filename.split(".")[0]
    return filename


data = common.get_file_contents("data/{}_input.txt".format(get_filename()))
test_data = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""


required_keys = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    #"cid"
]


def validate_passport(passport):
    """
    Ensure that the passport has all the right keys
    If so, its valid
    """
    valid = True
    for key in required_keys:
        if key not in passport.keys():
            valid = False
    return valid


def get_passports(lines):
    """
    Build list of passports by reading in the list
    passports are separated by blank lines
    we also normalize the passports by turning them into a single string
    for those that are on multiple lines
    """
    result = []
    passport = ""
    for line in lines:
        if len(line):
            passport += " " + line
        else:
            if len(passport):
                result.append(passport)
                passport = ""
    return result


def build_passport(data):
    """
    Takes in a string of key:value pairs separated by spaces
    and returns a dictionary
    """
    result = {}
    for part in data.split(" "):
        if ":" in part:
            parts = part.split(":")
            result[parts[0]] = parts[1]
    return result


def part1():
    passport_list = get_passports(data)
    result = []
    valid = 0
    for p in passport_list:
        passport = build_passport(p)
        if validate_passport(passport):
            valid += 1
    return valid


def part2():
    return "not complete"


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()

