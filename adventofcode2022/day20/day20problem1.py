input = []
with open('adventofcode2022/day20/day20example.txt') as file:
    for line in file:
        input.append(eval(line.strip()))
print(input)