ranges = []

# read input file
with open("adventofcode2025/day2/day2example.txt", "r") as input:
    for line in input:
        for range in line.strip().split(","):
            ranges.append(tuple([int(x) for x in range.split("-")]))

print(ranges[0])
