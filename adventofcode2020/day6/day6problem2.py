count = 0

with open('adventofcode2020\day6\day6input.txt', 'r') as input:
    customs_file = input.read().split('\n\n')

for line in customs_file:
    answer = line.replace('\n', ' ').split()
    key = set(answer[0])

    for i in answer[1:]:
        key = key.intersection(i)
    
    count += len(key)

print(count)