contents = []
with open('/data/data/com.termux/files/home/adventofcode/adventofcode2022/day3/day3example.txt', 'r') as input:
    for line in input:
        package = line.strip()
        first_half, second_half = package[:len(package)//2], package[len(package)//2:]
        contents.append([first_half,second_half])

# print(contents)

common = []
for rucksack in contents:
    common.append([value for value in rucksack[0] if value in rucksack[1]])

items = []
for c in common:
     items.append(''.join(set(c)))

# print(items)

priorities = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

# print(priorities)

total = 0
for item in items:
    total = total + priorities.index(item) + 1

print(total)
