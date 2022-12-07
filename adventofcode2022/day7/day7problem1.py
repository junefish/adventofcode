terminal_output = []
with open('adventofcode2022/day7/day7example.txt', 'r') as file:
    for line in file:
        terminal_output.append(line.strip())
# print(terminal_output)

commands = []
directories = []
sizes = []
for line in terminal_output:
    output = line.split(' ')
    if(line[0] == '$'):
        commands.append(line.split('$ ')[-1])
    elif(line[0] == 'd'):
        directories.append(output[-1])
    elif(line[0].isdigit()):
        sizes.append(int(output[0]))
print(commands)
print(directories)
print(sizes)