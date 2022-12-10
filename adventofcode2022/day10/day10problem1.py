signal = []
with open('adventofcode2022/day10/day10example1.txt', 'r') as file:
    for line in file:
        signal.append(line.strip())
        
# print(signal)

for command in signal:
    if(command=='noop'):
        continue
    elif(command.startswith('addx')):
        V = int(command.split(' ')[-1])
        print(V)