instructions = []

# read input file
with open("adventofcode2025/day1/day1example.txt", "r") as input:
    for line in input:
        instructions.append((line.strip()[0], int(line.strip()[1:])))

print(instructions[0])
