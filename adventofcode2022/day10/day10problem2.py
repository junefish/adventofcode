from collections import defaultdict

signal = []
with open('adventofcode2022/day10/day10input.txt', 'r') as file:
    for line in file:
        signal.append(line.strip())

cycles = defaultdict(int)
X = 1
cycle = 1
for command in signal:
    cycles[cycle] = X
    if(command=='noop'):
        cycle += 1
        cycles[cycle] = X
    elif(command.startswith('addx')):
        V = int(command.split(' ')[-1])
        for i in range(2):
            cycle += 1
            cycles[cycle] = X
        X += V
        cycles[cycle] = X

sprites = []
for(cycle,X) in cycles.items():
#     print(cycle,X)
    sprites.append(X)

output = ''
screen_width = 40
for i, value in enumerate(sprites):
    if sprites[i] in range((i % screen_width) - 1, (i % screen_width) + 2):
        output += "#"
    else:
        output += "."
    if (i + 1) % screen_width == 0:
        output += "\n"
print(output)