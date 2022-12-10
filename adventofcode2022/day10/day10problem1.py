signal = []
with open('adventofcode2022/day10/day10example1.txt', 'r') as file:
    for line in file:
        signal.append(line.strip())
        
# print(signal)

X = 1
cycle = 0
for command in signal:
    if(command=='noop'):
        cycle += 1
    elif(command.startswith('addx')):
        V = int(command.split(' ')[-1])
        cycle += 2
        X += V
    print(cycle,X)