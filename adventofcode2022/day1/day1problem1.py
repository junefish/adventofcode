items = []

with open('adventofcode2022/day1/day1example.txt', 'r') as input:
    for line in input:
        items.append(line.strip())

# print(items)
# print(items[0])

elves = [[]]

delimiter = ''
for item in items:
    if item == delimiter:
        elves.append([])
    elif item != delimiter: 
        elves[-1].append(item)
        
# print(elves)