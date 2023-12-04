# initialise lists
rounds = []
scores = []

# define scoring rules
outcomes = {"win": 6, "draw": 3, "loss": 0}
points = {"rock": 1, "paper": 2, "scissors": 3}
strategies = {"X": "lose", "Y": "draw", "Z": "win"}

# read input file
with open("adventofcode2022/day2/day2input.txt", "r") as input:
    for line in input:
        round = line.strip()
        rounds.append(round.split(" "))

# score game
for round in rounds:
    # opponent plays rock
    if round[0] == "A":
        # loss - rocks break scissors
        if round[1] == "X":
            choice = "scissors"
            result = outcomes["loss"]
        # draw - rock
        elif round[1] == "Y":
            choice = "rock"
            result = outcomes["draw"]
        # win - paper covers rock
        elif round[1] == "Z":
            choice = "paper"
            result = outcomes["win"]

    # opponent plays paper
    elif round[0] == "B":
        # loss - paper covers rock
        if round[1] == "X":
            choice = "rock"
            result = outcomes["loss"]
        # draw - paper
        elif round[1] == "Y":
            choice = "paper"
            result = outcomes["draw"]
        # win - scissors cut paper
        elif round[1] == "Z":
            choice = "scissors"
            result = outcomes["win"]

    # opponent plays scissors
    elif round[0] == "C":
        # loss - scissors cut paper
        if round[1] == "X":
            choice = "paper"
            result = outcomes["loss"]
        # draw - scissors
        elif round[1] == "Y":
            choice = "scissors"
            result = outcomes["draw"]
        # win - rock breaks scissors
        elif round[1] == "Z":
            choice = "rock"
            result = outcomes["win"]

    # calculate score
    score = result + points[choice]
    scores.append(score)

# print total score
print(sum(scores))
