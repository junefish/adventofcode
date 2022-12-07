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
# print(drawing)
crates = []
for line in drawing:
    crates.append([line[containers * 4 + 1] for containers in range(len(line) // 4 + 1)])    
# print(crates)
crate_stack = []
crate_stack = [list("".join(stack_column).strip()[::-1]) for stack_column in zip(*crates)]
# print(crate_stack)

procedure = []
for step in instructions[1]:
    step = step.split(' ')
    step.remove('move')
    step.remove('from')
    step.remove('to')
    procedure.append(step)

# print(procedure)

for step in procedure:
    times = int(step[0])
    start = int(step[1])
    end = int(step[2])

    i = times
    while i > 0:
        crate = crate_stack[start-1].pop()
        crate_stack[end-1].append(crate)
        i = i-1
    print(crate_stack)