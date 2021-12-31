from typing import Counter


with open('adventofcode2021\day5\day5input.txt', 'r') as input:
  lines = input.read().splitlines()

all_points = []
for line in lines:
    point1, point2 = line.split('->')
    x1, y1 = tuple(map(int, point1.split(',')))
    x2, y2 = tuple(map(int, point2.split(',')))

    if(x1 == x2 or y1 == y2):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range (min(y1, y2), max(y1, y2) + 1):
                all_points.append((x,y))

    else:
        x_increment = 1 if x1 < x2 else -1
        y_increment = 1 if y1 < y2 else -1

        y = y1
        for x in range(x1, x2 + x_increment, x_increment):
            all_points.append((x,y))
            y += y_increment

print(len([point for point in Counter(all_points).values() if point > 1]))