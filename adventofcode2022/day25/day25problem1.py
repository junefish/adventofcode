requirements = [[]]
with open("adventofcode2022/day25/day25example.txt") as file:
    for line in file:
        for char in line:
            if char == "\n":
                requirements.append([])
            elif not char.isnumeric():
                requirements[-1].append(char)
            else:
                requirements[-1].append(eval(char))
print(requirements)
