heightmap = []
with open('adventofcode2022/day12/day12example.txt', 'r') as input:
    for line in input:
        x = [*line.strip()]
        heightmap.append(x)
# print(heightmap)

for i,_ in enumerate(heightmap):
    for j,_ in enumerate(heightmap[0]):
        if(heightmap[i][j] == 'S'):
            start = (i,j)
        if(heightmap[i][j] == 'E'):
            end = (i,j)
print(start)
# print(end)