import re

with open("adventofcode2024/day3/day3example.txt", "r") as input:
    memory = input.readlines()[0]


def scan(str):
    substring = "mul\(\d+,\d+\)"
    result = re.findall(substring, str)
    return result


instructions = scan(memory)


def mul(step):
    s = re.split(r"\(|\,|\)", step)
    product = int(s[1]) * int(s[2])
    return product


result = 0
for step in instructions:
    result += mul(step)

print(result)
