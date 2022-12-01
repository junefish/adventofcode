items = []

with open('adventofcode2022/day1/day1input.txt', 'r') as input:
    for line in input:
        item = line.split('\n\n')
        items.append(item[0])

elves = [[]]*(items.count('\n')+1)
