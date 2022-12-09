terminal_output = []
with open('adventofcode2022/day7/day7example.txt', 'r') as file:
    for line in file:
        terminal_output.append(line.strip())
# print(terminal_output)

filepath = []

for line in terminal_output:
    # change directories
    if(line.startswith('$ cd')):
        directory = line.split()[-1]
        # go to previous directory
        if(directory == '..'):
            filepath.pop()
        # add directory to filepath
        else:
            filepath.append(directory)
    print(''.join(filepath))