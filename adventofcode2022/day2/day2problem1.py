rounds = []
with open('adventofcode2022/day2/day2example.txt', 'r') as input:
    for line in input:
        round = (line.strip())
        rounds.append(round.split(' '))
        
# print(rounds)

points = {'X': 1, 'Y': 2, 'Z': 3}

# print(points['A'])

outcomes = {'win': 6, 'draw': 3, 'loss': 0}

scores = []

for round in rounds:
    if(round[0] == 'A'):
        if(round[1] == 'X'):
            result = outcomes['draw']
        elif(round[1] == 'Y'):
            result = outcomes['win']
        elif(round[1] == 'Z'):
            result = outcomes['loss']
    elif(round[0] == 'B'):
        if(round[1] == 'X'):
            result = outcomes['loss']
        elif(round[1] == 'Y'):
            result = outcomes['draw']
        elif(round[1] == 'Z'):
            result = outcomes['win']
    elif(round[0] == 'C'):
        if(round[1] == 'X'):
            result = outcomes['win']
        elif(round[1] == 'Y'):
            result = outcomes['loss']
        elif(round[1] == 'Z'):
            result = outcomes['draw']
    score = result + points[round[1]]
    scores.append(score)
    
print(sum(scores))