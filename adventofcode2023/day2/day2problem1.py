games = []

with open("adventofcode2023/day2/day2example.txt", "r") as input:
    for line in input:
        ID = int(line.strip().split(":")[0].split(" ")[1])

        moves = line.strip().split(": ")[1]

        games.append([ID, moves])

print(games)
