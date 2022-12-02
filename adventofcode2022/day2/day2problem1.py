# initialise lists
rounds = []
scores = []

# define scoring rules
outcomes = {'win': 6, 'draw': 3, 'loss': 0}
points = {'X': 1, 'Y': 2, 'Z': 3}

# read input file
with open('adventofcode2022/day2/day2example.txt', 'r') as input:
    for line in input:
        round = (line.strip())
        rounds.append(round.split(' '))
        
# score game
for round in rounds:
    # opponent plays rock
    if(round[0] == 'A'):
        # rocks
        if(round[1] == 'X'):
            result = outcomes['draw']
        # paper covers rock
        elif(round[1] == 'Y'):
            result = outcomes['win']
        # rock breaks scissors
        elif(round[1] == 'Z'):
            result = outcomes['loss']
            
    # opponent plays paper
    elif(round[0] == 'B'):
        # paper covers rock
        if(round[1] == 'X'):
            result = outcomes['loss']
        # papers
        elif(round[1] == 'Y'):
            result = outcomes['draw']
        # scissors cut paper
        elif(round[1] == 'Z'):
            result = outcomes['win']
            
    # opponent plays scissors
    elif(round[0] == 'C'):
        # rock beats scissors
        if(round[1] == 'X'):
            result = outcomes['win']
        # scissors cut paper
        elif(round[1] == 'Y'):
            result = outcomes['loss']
        # scissors
        elif(round[1] == 'Z'):
            result = outcomes['draw']
    
    # calculate score
    score = result + points[round[1]]
    scores.append(score)

# print total score    
print(sum(scores))