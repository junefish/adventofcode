import re

with open("adventofcode2024/day3/day3example2.txt", "r") as input:
    memory = "".join(input.readlines())

# print(memory)

instructions = re.sub("don't\(\)", ".no.", re.sub("do\(\)", ".yes.", memory)).split(".")
# print(instructions)


def parse_commands(list):
    valid = [list[0]]

    i = 0
    while i < len(list) - 1:
        i += 1
        if list[i] == "yes":
            continue
        elif list[i] == "no":
            while list[i] != "yes":
                i += 1
        else:
            valid.append(list[i])

    return valid


valid_instructions = parse_commands(instructions)

print(valid_instructions)
