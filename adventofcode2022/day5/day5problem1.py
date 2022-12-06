input = []

# read input file
with open('adventofcode2022/day5/day5example.txt', 'r') as file:
    for line in file:
        # line = line.strip()
        input.append(line)

instructions = [[]]
delimiter = '\n'
for line in input:
    if line == delimiter:
        instructions.append([])
    elif line != delimiter: 
        instructions[-1].append(line.split('\n')[0])
        
drawing = instructions[0]

procedure = []
for step in instructions[1]:
    step = step.split(' ')
    step.remove('move')
    step.remove('from')
    step.remove('to')
    procedure.append(step)

print(procedure)