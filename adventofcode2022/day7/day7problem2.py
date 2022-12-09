from collections import defaultdict

terminal_output = []
filepath = []
sizes = defaultdict(int)

with open('adventofcode2022/day7/day7example.txt', 'r') as file:
    for line in file:
        terminal_output.append(line.strip())

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
    
    # list contents
    elif(line.startswith('$ ls')):
        continue
    
    # parse ls output for sizes
    else:
        size, _ = line.split()
        if(size.isdigit()):
            size = int(size)
            for i in range(len(filepath)):
                sizes['/'.join(filepath[:i+1])] += size