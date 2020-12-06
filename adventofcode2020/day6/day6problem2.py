answers = []


# open file
with open('adventofcode2020\day6\day6input.txt', 'r') as input:
    customs_file = input.read().split('\n\n')

for line in customs_file:
    answers.append(line.split('\n'))

for answer in answers:
    keys = list(answer[0])
    i = 1
    count = 0
    for key in keys:
        if(key in answer[i]):
            count += 1
        else:
            break

