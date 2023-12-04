monkeys = {}
with open("adventofcode2022/day21/day21example.txt") as input:
    for line in input:
        name = line.strip().split(": ")[0]
        info = line.strip().split(": ")[1]

        if info.isnumeric():
            i = eval(info)
        else:
            i = info.split(" ")

        monkeys.update({name: i})
print(monkeys)
print(monkeys["root"])
