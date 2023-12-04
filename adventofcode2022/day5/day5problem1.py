# initialise lists
input = []
instructions = [[]]
crates = []
crate_stacks = []
procedure = []

# read input file
with open("adventofcode2022/day5/day5input.txt", "r") as file:
    for line in file:
        input.append(line)

# split instructions in half into drawing & procedure
delimiter = "\n"
for line in input:
    if line == delimiter:
        instructions.append([])
    elif line != delimiter:
        instructions[-1].append(line.split("\n")[0])

# parse drawing into stacks of crates
drawing = instructions[0]
# parse row into crates
for line in drawing:
    crates.append(
        [line[containers * 4 + 1] for containers in range(len(line) // 4 + 1)]
    )
# transpose rows into columns (stacks)
crate_stacks = [
    list("".join(stack_column).strip()[::-1]) for stack_column in zip(*crates)
]

# clean up steps into array
for step in instructions[1]:
    step = step.split(" ")
    step.remove("move")
    step.remove("from")
    step.remove("to")
    procedure.append(step)

# follow steps to rearrange crates
for step in procedure:
    times = int(step[0])
    start = int(step[1])
    end = int(step[2])

    i = times
    while i > 0:
        crate = crate_stacks[start - 1].pop()
        crate_stacks[end - 1].append(crate)
        i = i - 1

# find top crate on each stack
top = ""
for i in range(len(crate_stacks)):
    top = "".join([top, crate_stacks[i].pop()])

# print answer
print(top)
