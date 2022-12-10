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

signal_strength = {}
for(cycle,X) in cycles.items():
    signal_strength[cycle] = cycle * X

interesting_cycles = [20,60,100,140,180,220]
for cycle in interesting_cycles:
    print(signal_strength[cycle])