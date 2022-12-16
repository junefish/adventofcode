heightmap = []
with open('adventofcode2022/day12/day12example.txt', 'r') as input:
    for line in input:
        x = [*line.strip()]
        heightmap.append(x)
# print(heightmap)

start = (0,0)
for i,_ in enumerate(heightmap):
    for j,_ in enumerate(heightmap[0]):
        if(heightmap[i][j] == 'E'):
            end = (i,j)
            break
print(end)