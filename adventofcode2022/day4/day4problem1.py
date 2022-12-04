assignments = []
with open('adventofcode2022/day4/day4example.txt', 'r') as input:
    for line in input:
        line = line.strip()
        assignments.append(line.split(','))
        
# print(assignments)

contains = 0
for pair in assignments:
    elf1,elf2 = pair[0],pair[-1]
    print(elf1,elf2)
    
    start1,end1 = elf1.split('-')
    start2,end2 = elf2.split('-')
    print(start1,end1)
    print(start2,end2)