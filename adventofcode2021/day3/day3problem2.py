from statistics import mode

diagnostics = []
with open('adventofcode2021\day3\day3example.txt', 'r') as input:
  for line in input:
    item = line.split('\n')
    diagnostics.append(str(item[0]))

digits = []
for i in range(len(diagnostics)):
    digits.append(list(diagnostics[i]))

number_length = len(digits[0])
digit_lists = [[] for x in range(number_length)]

for entry in digits:
    for i in range(number_length):
        digit_lists[i].append(entry[i])

oxygen_test = diagnostics
for i in range(len(digit_lists)):
    digit = digit_lists[i]
    bit = ['1' for x in range(number_length)]
    if(digit.count('0') != digit.count('1')):
        bit[i] = str(mode(digit))
print(bit)