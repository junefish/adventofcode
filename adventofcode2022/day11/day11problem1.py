monkeys = [[]]
delimiter = '\n'
with open('adventofcode2022/day11/day11example.txt', 'r') as input:
    for line in input:
        # notes.append(line.strip())
        if line == delimiter:
            monkeys.append([])
        elif line.startswith('Monkey'):
            continue
        elif line != delimiter: 
            monkeys[-1].append(line.strip())

print(monkeys)