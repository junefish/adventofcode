passports = []

with open("adventofcode2020\day4\day4input.txt", "r") as input:
    passport_file = input.read().split("\n\n")
    for line in passport_file:
        passports.append(line.replace("\n", " "))

valid_passports = 0
keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for passport in passports:
    if all(key + ":" in passport for key in keys):
        valid_passports += 1

print(valid_passports)
