forest = []
with open('adventofcode2022/day8/day8example.txt', 'r') as file:
    for line in file:
        treeline = (line.strip())
        forest.append([*treeline])
    forest = [list(map(int, x)) for x in forest]
 
print(forest)
