import os
import common


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


def is_inbetween(val, start, end):
    return start <= val <= end


def get_height(val):
    if "in" in val:
        return {"val": int(val.replace("in", "")), "type": "inch"}
    else:
        return {"val": int(val.replace("cm", "")), "type": "cm"}


def is_valid_color(color):
    if "#" not in color:
        return False
    valid_characters = ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for character in color[1:]:
        if character not in valid_characters:
            print("Character not in valid characters: {}".format(character))
            return False
    return True


def validate_password_better(passport):
    if not validate_passport(passport):
        return False

    for k, v in passport.items():
        if k == "byr":
            val = int(passport[k])
            if not is_inbetween(val, 1920, 2002):
                return False
        elif k == "iyr":
            val = int(passport[k])
            if not is_inbetween(val, 2010, 2020):
                return False
        elif k == "eyr":
            val = int(passport[k])
            if not is_inbetween(val, 2020, 2030):
                return False
        elif k == "hgt":
            height = get_height(v)
            if height["type"] == "cm":
                if not is_inbetween(height["val"], 150, 193):
                    return False
            else:
                if not is_inbetween(height["val"], 59, 76):
                    return False
        elif k == "hcl":
            if not is_valid_color(v):
                return False
        elif k == "ecl":
            valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if v not in valid_colors:
                return False
        elif k == "pid":
            if len(v) != 9:
                return False
    return True


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
    real_file = os.path.join("..", "data", "day04_input.txt")
    data = common.get_file_contents(real_file)

    passport_list = get_passports(data)
    valid = 0
    for p in passport_list:
        passport = build_passport(p)
        if validate_passport(passport):
            valid += 1
    return valid


def part2():
    real_file = os.path.join("..", "data", "day04_input.txt")
    data = common.get_file_contents(real_file)

    valid = 0
    passport_list = get_passports(data)
    for p in passport_list:
        passport = build_passport(p)
        if validate_password_better(passport):
            valid += 1
    return valid


def main():
    part1_answer = part1()
    part2_answer = part2()

    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


if __name__ == '__main__':
    main()
