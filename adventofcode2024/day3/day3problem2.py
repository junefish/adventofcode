import re

with open("adventofcode2024/day3/day3example2.txt", "r") as input:
    memory = "".join(input.readlines())

# print(memory)

instructions = re.sub("don't\(\)", ".no.", re.sub("do\(\)", ".yes.", memory)).split(".")
print(instructions)
