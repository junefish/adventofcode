answers = []

# open file
with open('adventofcode2020\day6\day6input.txt', 'r') as input:
    customs_file = input.read().split('\n\n')

for line in customs_file:
    answers.append(line.replace('\n', ''))
            
# remove duplicate answers within a group
uniques = []
for answer in answers:
    uniques.append("".join(set(answer)))

groups = []

for item in uniques:
    groups.append(len(item))

print(sum(groups))