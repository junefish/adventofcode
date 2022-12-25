map = []
with open('adventofcode2022/day24/day24example.txt') as input:
    for line in input:
        map.append([*line.strip()])
print(map)