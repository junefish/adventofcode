entries = []

with open('adventofcode2020\day2\day2input.txt', 'r') as input:
  for line in input:
    item = line.split('\n')
    entries.append(item[0])

print(entries)