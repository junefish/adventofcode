movements = []
# read input file
with open('adventofcode2022/day9/day9example.txt', 'r') as file:
    for line in file:
        dir, dist = line.strip().split()
        movements.append((dir,int(dist)))
print(movements)