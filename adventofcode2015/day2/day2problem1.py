dimensions = []

# read input file
with open('adventofcode2015/day2/day2example.txt', 'r') as input:
    for line in input:
        dimensions.append((line.strip().split('x')))

for present in dimensions:
    length = int(present[0])
    width = int(present[1])
    height = int(present[2])

    area = 2*length*width + 2*width*height + 2*height*length

    slack = min(length*width, width*height, height*length)
    print(slack)