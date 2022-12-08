trees = []
with open('adventofcode2022/day8/day8example.txt', 'r') as file:
    for line in file:
        treeline = (line.strip())
        trees.append([*treeline])
    trees = [list(map(int, x)) for x in trees]
 
print(trees)
