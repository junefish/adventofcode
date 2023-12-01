calibrations = []

# read input file
with open('adventofcode2023/day1/day1example2.txt', 'r') as input:
    for line in input:
        calibrations.append(line.strip())

# print(calibrations)

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

for value in calibrations:
    for key,num in digits.items():
        if(key in value):
            print(key)