from statistics import mode

diagnostics = []
with open('adventofcode2021\day3\day3input.txt', 'r') as input:
  for line in input:
    item = line.split('\n')
    diagnostics.append(str(item[0]))

digits = []
for i in range(0, len(diagnostics)):
    digits.append(list(diagnostics[i]))

number_length = len(digits[0])
digit_lists = [[] for x in range(number_length)]

for entry in digits:
    for i in range(number_length):
        digit_lists[i].append(entry[i])

gamma = epsilon = ""
for digit in digit_lists:
    gamma += str(mode(digit))

binary_inversion = {'0': '1', '1': '0'}
for char in gamma:
    epsilon += binary_inversion[char]

print(int(gamma, 2) * int(epsilon, 2))