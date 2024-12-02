reports = []
with open("adventofcode2024/day2/day2example.txt", "r") as input:
    for line in input:
        reports.append([int(item) for item in line.strip().split(" ")])

print(reports)
