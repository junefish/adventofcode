contents = []
with open('adventofcode2022/day3/day3input.txt', 'r') as input:
    for line in input:
        contents.append(line.strip())

# print(contents)

group_size = 3
groups = [contents[i:i + group_size] for i in range(0, len(contents), group_size)]

# print(groups[0])
# print(groups)

common = []
for rucksack in groups:
    common.append([value for value in rucksack[0] if value in rucksack[1] and value in rucksack[2]])
    
# print(common)

items = []
for c in common:
     items.append(''.join(set(c)))
     
print(items)

priorities = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

total = 0
for item in items:
    total = total + priorities.index(item) + 1

print(total)