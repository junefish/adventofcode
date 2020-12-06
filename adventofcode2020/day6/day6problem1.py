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

groups = dict.fromkeys(uniques)

# count number of answers per group
for key, value in groups.items():
    groups[key] = len(key)

# calculate sum of answers from all groups
print(sum(groups.values()))