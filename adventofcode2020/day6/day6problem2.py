answers = []


# open file
with open('adventofcode2020\day6\day6input.txt', 'r') as input:
    customs_file = input.read().split('\n\n')

for line in customs_file:
    answers.append(line.split('\n'))

# print(answers)

for answer in answers:
    count = 0
    keys = list(answer[0])
    if(len(answers) == 1):
        count = answer[0]
    else:
        break
        # i = 1
        # while(i < len(answers)):
        #     if all(key in answer[i] for key in keys):
        #         count += 1
print(count)