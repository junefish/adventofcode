depths = []

with open("adventofcode2021\day1\day1input.txt", "r") as input:
    for line in input:
        item = line.split("\n")
        depths.append(int(item[0]))

deltas = []
for i in range(0, len(depths)):
    if i == 0:
        delta = "N/A - no previous measurement"
    elif depths[i] > depths[i - 1]:
        delta = "increased"
    elif depths[i] < depths[i - 1]:
        delta = "decreased"
    deltas.append(delta)

print(deltas.count("increased"))
