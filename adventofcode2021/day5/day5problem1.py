with open('adventofcode2021\day5\day5example.txt', 'r') as input:
  lines = input.read().splitlines()

print(lines)

for line in lines:
    point1, point2 = line.split('->')
    x1, y1 = tuple(map(int, point1.split(',')))
    x2, y2 = tuple(map(int, point2.split(',')))

    print(x1, y1, x2, y2)