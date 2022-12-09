forest = []
with open('adventofcode2022/day8/day8example.txt', 'r') as file:
    for line in file:
        treeline = (line.strip())
        forest.append([*treeline])
    forest = [list(map(int, x)) for x in forest]
 
# print(forest)

# trees around the edge of the grid
visible = (len(forest)-1)*4
print(visible)
