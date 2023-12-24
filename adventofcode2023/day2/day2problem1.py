games = []

with open("adventofcode2023/day2/day2example.txt", "r") as input:
    for line in input:
        games.append(line.strip())

print(games)
