cubes = []
with open("adventofcode2022/day18/day18example.txt") as input:
    for line in input:
        cubes.append([int(i) for i in line.strip().split(",")])
print(cubes)
