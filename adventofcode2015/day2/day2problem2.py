dimensions = []

# read input file
with open('adventofcode2015/day2/day2example.txt', 'r') as input:
    for line in input:
        dimensions.append((line.strip().split('x')))

ribbon = 0
for present in dimensions:
    length = int(present[0])
    width = int(present[1])
    height = int(present[2])

    sides = [length, width, height]
    wrap = 2*sorted(sides)[0] + 2*sorted(sides)[1]

    bow = length*width*height

    ribbon += wrap + bow

print(ribbon)