from typing import Counter


with open("adventofcode2021\day5\day5input.txt", "r") as input:
    lines = input.read().splitlines()

# print(lines)

all_points = []
for line in lines:
    point1, point2 = line.split("->")
    x1, y1 = tuple(map(int, point1.split(",")))
    x2, y2 = tuple(map(int, point2.split(",")))

    # print(x1, y1, x2, y2)

    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                all_points.append((x, y))

print(len([point for point in Counter(all_points).values() if point > 1]))
