left = []
right = []

with open("adventofcode2024/day1/day1example.txt", "r") as input:
    for line in input:
        left.append(int(line.strip().split(" ")[0]))
        right.append(int(line.strip().split(" ")[-1]))
