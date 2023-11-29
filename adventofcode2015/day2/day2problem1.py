dimensions = []

# read input file
with open('adventofcode2015/day2/day2example.txt', 'r') as input:
    for line in input:
        dimensions.append((line.strip().split('x')))
print(dimensions)