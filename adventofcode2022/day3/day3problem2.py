# initialise lists
contents = []
common = []
items = []

# read input file
with open("adventofcode2022/day3/day3input.txt", "r") as input:
    for line in input:
        contents.append(line.strip())

# split contents into groups of 3
group_size = 3
groups = [contents[i : i + group_size] for i in range(0, len(contents), group_size)]

# find items in common within group members
for rucksack in groups:
    common.append(
        [
            value
            for value in rucksack[0]
            if value in rucksack[1] and value in rucksack[2]
        ]
    )

# reduce to unique items
for c in common:
    items.append("".join(set(c)))

# define priorities
priorities = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

# calculate sum of priorities for common items
total = 0
for item in items:
    total = total + priorities.index(item) + 1

# print answer
print(total)
