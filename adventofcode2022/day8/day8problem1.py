forest = []
with open('adventofcode2022/day8/day8input.txt', 'r') as file:
    for line in file:
        treeline = (line.strip())
        forest.append([*treeline])
    forest = [list(map(int, x)) for x in forest]
 
# print(forest)

# # trees around the edge of the grid
# visible = (len(forest)-1)*4
# print(visible)

# tranpose forest for easier parsing
forest2 = list(zip(*forest))

visible = 0
for i in range(len(forest[0])):
    for j in range(len(forest)):
        tree = forest[i][j]
        if all(x < tree for x in forest[i][0:j]) or \
            all(x < tree for x in forest[i][j+1:]) or \
            all(x < tree for x in forest2[j][0:i]) or \
            all(x < tree for x in forest2[j][i+1:]):
            visible += 1
            
print(visible)