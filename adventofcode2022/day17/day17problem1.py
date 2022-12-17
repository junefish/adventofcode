jets = []
with open('adventofcode2022/day17/day17example.txt') as input:
    for line in input:
        for char in line:
            jets.append(char)
print(jets)