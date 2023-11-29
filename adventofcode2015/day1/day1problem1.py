instructions = []

# read input file
with open('adventofcode2015/day1/day1input.txt', 'r') as input:
    for line in input:
        instructions += line.strip()

floor = 0
for char in instructions:
    if(char == '('):
        floor += 1
    elif(char == ')'):
        floor -= 1
print(floor)