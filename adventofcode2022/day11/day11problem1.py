notes = []
with open('adventofcode2022/day11/day11example.txt', 'r') as input:
    for line in input:
        notes.append(line.strip())
        
monkeys = [[]]
delimiter = '\n'
for line in notes:
    if line == delimiter:
        monkeys.append([])
    elif line != delimiter: 
        monkeys[-1].append(line)
print(monkeys[0])