# initialise lists
items = []
elves = [[]]
calories = []

# read input file
with open("adventofcode2022/day1/day1input.txt", "r") as input:
    for line in input:
        items.append(line.strip())

# assign items to elves
delimiter = ""
for item in items:
    if item == delimiter:
        elves.append([])
    elif item != delimiter:
        elves[-1].append(int(item))

# calculate calories carried per elf
for elf in elves:
    calories.append(sum(elf))

# print the max calories carried by an elf
print(max(calories))
