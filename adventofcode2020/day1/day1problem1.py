entries = []

with open('adventofcode2020\day1\day1input.txt', 'r') as input:
  for line in input:
    item = line.split('\n')
    entries.append(int(item[0]))

for i in range(len(entries)):
    for j in range(len(entries)):
        sum = entries[i] + entries[j]
        if(sum) == 2020:
            print(entries[i] * entries[j])
            break