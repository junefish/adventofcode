heightmap = []
with open('adventofcode2022/day12/day12example.txt', 'r') as input:
    for line in input:
        x = [*line.strip()]
        heightmap.append(x)
print(heightmap)