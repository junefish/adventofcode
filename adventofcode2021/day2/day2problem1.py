commands = []
with open('adventofcode2021\day2\day2input.txt', 'r') as input:
  for line in input:
    item = line.split('\n')
    command = (item[0].split(' '))
    commands.append((str(command[0]), int(command[1])))
# print(commands)

horizontal = 0
depth = 0
for command in commands:
    #print(command)
    if(command[0] == 'forward'):
        horizontal += command[1]
    elif(command[0] == 'down'):
        depth += command[1]
    elif(command[0] == 'up'):
        depth += command[1]
    #print(horizontal,depth)
print(horizontal * depth)