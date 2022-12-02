# initialise lists
rounds = []
scores = []

# define scoring rules
outcomes = {'win': 6, 'draw': 3, 'loss': 0}
points = {'X': 1, 'Y': 2, 'Z': 3}

# read input file
with open('adventofcode2022/day2/day2input.txt', 'r') as input:
    for line in input:
        round = (line.strip())
        rounds.append(round.split(' '))