import re

passports = []

with open("adventofcode2020\day4\day4input.txt", "r") as input:
    passport_file = input.read().split("\n\n")
    for line in passport_file:
        passports.append(line.replace("\n", " "))

passport_items = []
keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for passport in passports:
    if all(key + ":" in passport for key in keys):
        #        complete_passports.append(passport)
        res = re.split(":| ", passport)
        passport_items.append({res[i]: res[i + 1] for i in range(0, len(res) - 1, 2)})

# passport_items = []
# for item in complete_passports:
#    res = re.split(':| ', item)
#    passport_items.append({res[i]: res[i+1] for i in range(0, len(res) - 1, 2)})

valid_passports = 0
for passport in passport_items:
    if (
        int(passport["byr"]) >= 1920
        and int(passport["byr"]) <= 2002
        and int(passport["iyr"]) >= 2010
        and int(passport["iyr"]) <= 2020
        and int(passport["eyr"]) >= 2020
        and int(passport["eyr"]) <= 2030
        and re.match(
            "^(1([5-8][0-9]|9[0-3])cm|(59|[6][0-9]|[7][0-6])in)$", passport["hgt"]
        )
        and re.match("#[0-9a-f]{6}", passport["hcl"])
        and re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", passport["ecl"])
        and re.match("^\d{9}$", passport["pid"])
    ):
        valid_passports += 1

print(valid_passports)
