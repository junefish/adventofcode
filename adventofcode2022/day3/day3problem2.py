contents = []
with open('adventofcode2022/day3/day3input.txt', 'r') as input:
    for line in input:
        contents.append(line.strip())

# print(contents)

group_size = 3
groups = [contents[i:i + group_size] for i in range(0, len(contents), group_size)]

# print(groups[0])
# print(groups)

priorities = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')