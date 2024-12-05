import re

with open("adventofcode2024/day3/day3example.txt", "r") as input:
    memory = input.readlines()[0]

# print(memory)


def scan(str):
    substring = "mul\(\d+,\d+\)"
    result = re.findall(substring, str)
    return result


print(scan(memory))
