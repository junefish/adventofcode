from statistics import mode

diagnostics = []
with open("adventofcode2021\day3\day3example.txt", "r") as input:
    for line in input:
        item = line.split("\n")
        diagnostics.append(str(item[0]))

number_length = len(diagnostics[0])
digit_lists = [[] for x in range(number_length)]

oxygen_test = diagnostics
oxygen_mode = digit_lists
for i in len(oxygen_test):
    for j in range(number_length):
        oxygen_mode[i][j].append(oxygen_test[i][j])

print(oxygen_mode)
