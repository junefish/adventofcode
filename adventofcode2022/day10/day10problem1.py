# import modules
from collections import defaultdict

# initialise lists
signal = []
cycles = defaultdict(int)
signal_strength = {}

# define variables
X = 1
cycle = 1
interesting_cycles = [20,60,100,140,180,220]
total = 0

# read input file
with open('adventofcode2022/day10/day10input.txt', 'r') as file:
    for line in file:
        signal.append(line.strip())
        
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
    signal_strength[cycle] = cycle * X

for cycle in interesting_cycles:
    total += signal_strength[cycle]

print(total)