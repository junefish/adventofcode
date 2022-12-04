# initialise lists
contents = []
common = []
items = []

# read input file
with open('adventofcode2022/day3/day3input.txt', 'r') as input:
    for line in input:
        package = line.strip()
        first_half, second_half = package[:len(package)//2], package[len(package)//2:]
        contents.append([first_half,second_half])

# find items in common between compartments
for rucksack in contents:
    common.append([value for value in rucksack[0] if value in rucksack[1]])

# reduce common items for uniqueness
for c in common:
     items.append(''.join(set(c)))

# define priorities
priorities = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

# find sum of priorities from common items
total = 0
for item in items:
    total = total + priorities.index(item) + 1

# print answer
print(total)