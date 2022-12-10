from collections import defaultdict

signal = []
with open('adventofcode2022/day10/day10example2.txt', 'r') as file:
    for line in file:
        signal.append(line.strip())
        
# print(signal)

X = 1
cycle = 1
cycles = defaultdict(int)
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


for(cycle,X) in cycles.items():
    print(cycle,X)