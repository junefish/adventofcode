from statistics import mode

diagnostics = []
with open('adventofcode2021\day3\day3example.txt', 'r') as input:
  for line in input:
    item = line.split('\n')
    diagnostics.append(str(item[0]))

digits = []
for i in range(0, len(diagnostics)):
    digits.append(list(diagnostics[i]))

oxygen_test = digits
print(oxygen_test)