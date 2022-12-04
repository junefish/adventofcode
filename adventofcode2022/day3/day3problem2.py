contents = []
with open('adventofcode2022/day3/day3input.txt', 'r') as input:
    for line in input:
        contents.append(line.strip())

print(contents)

priorities = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')