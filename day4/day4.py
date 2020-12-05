import re

passports = []
keys = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]


def read_input():
    passport = ""
    with open("input.txt") as file:
        for line in file:
            if line.rstrip("\n"):
                passport += " " + line.rstrip("\n")
            else:
                passports.append(passport)
                passport = ""
    passports.append(passport)


def validate_keys(passport_string):
    pairs = passport_string.split(" ")
    valid = True
    for pair in pairs:
        if pair:
            key, value = pair.split(":")
            if key == "byr" and not int(value) in range(1920, 2003):
                valid = False
            if key == "iyr" and not int(value) in range(2010, 2021):
                valid = False
            if key == "eyr" and not int(value) in range(2020, 2031):
                valid = False
            if key == "hgt" and (not ((value.endswith("in") and int(value.rstrip("in")) in range(59, 77))
                                      or value.endswith("cm") and int(value.rstrip("cm")) in range(150, 194))):
                valid = False
            if key == "hcl" and (not re.search(r"#[0-9a-f]{6}", value) or len(value) != 7):
                valid = False
            if key == "ecl" and value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                valid = False
            if key == "pid" and (not re.search(r"[0-9]{9}", value) or len(value) != 9):
                valid = False
    return valid


def check_passports(validation_on=False):
    count = 0
    for p in passports:
        contains_keys = True

        for key in keys:
            if key not in p:
                contains_keys = False

        if contains_keys:
            if validation_on:
                if validate_keys(p):
                    count += 1
            else:
                count += 1
    return count


if __name__ == '__main__':
    read_input()
    print(check_passports(), check_passports(True))


