commands = []
with open("adventofcode2021\day2\day2input.txt", "r") as input:
    for line in input:
        item = line.split("\n")
        command = item[0].split(" ")
        commands.append((str(command[0]), int(command[1])))

horizontal = 0
depth = 0
aim = 0
for command in commands:
    X = command[1]
    if command[0] == "down":
        aim += X
    elif command[0] == "up":
        aim -= X
    elif command[0] == "forward":
        horizontal += X
        depth += aim * X

print(horizontal * depth)
