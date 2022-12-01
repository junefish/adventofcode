items = []

with open('adventofcode2022/day1/day1input.txt', 'r') as input:
    for line in input:
        items.append(line.strip())

# print(items)
# print(items[0])

elves = [[]]*(items.count('')+1)

# print(len(elves))