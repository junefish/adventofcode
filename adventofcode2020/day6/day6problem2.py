answers = []
count = 0

with open('adventofcode2020\day6\day6input.txt', 'r') as input:
    customs_file = input.read().splitlines()

for line in customs_file:
    if(line == ''):
        count += len(set.intersection(*answers))
        answers = []
    else:
        answers.append(set(line))

print(count)