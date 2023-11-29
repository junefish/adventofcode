instructions = []

# read input file
with open('adventofcode2015/day1/day1example.txt', 'r') as input:
    for line in input:
        instructions += line.strip()
    print(instructions)

for char in instructions:
    if(char == '('):
        print(char + " is an open paren")
    elif(char == ')'):
        print(char + " is a closed paren")