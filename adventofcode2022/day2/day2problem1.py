rounds = []
with open('adventofcode2022/day2/day2example.txt', 'r') as input:
    for line in input:
        rounds.append(line.strip().split(' '))
        
print(rounds)