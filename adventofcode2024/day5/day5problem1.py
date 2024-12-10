rules = []
updates = []

with open("adventofcode2024/day5/day5example.txt", "r") as file:
    input = "".join(file.readlines()).split('\n\n')
    for r in input[0].split('\n'):
        rules.append(r.split('|'))
    for u in input[1].split('\n'):
        updates.append(u.split(','))
print(rules)
print(updates)