assignments = []
with open('adventofcode2022/day4/day4example.txt', 'r') as input:
    for line in input:
        line = line.strip()
        assignments.append(line.split(','))
        
print(assignments)