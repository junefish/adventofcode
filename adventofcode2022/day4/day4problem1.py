assignments = []
with open('adventofcode2022/day4/day4input.txt', 'r') as input:
    for line in input:
        line = line.strip()
        assignments.append(line.split(','))
        
# print(assignments)

contains = 0
for pair in assignments:
    elf1,elf2 = pair[0],pair[-1]
    # print(elf1,elf2)
    
    start1,end1 = elf1.split('-')
    start2,end2 = elf2.split('-')
    # print(start1,end1)
    # print(start2,end2)
    start1 = int(start1)
    start2 = int(start2)
    end1 = int(end1)
    end2 = int(end2)
    
    # check if elf 1's range contains elf 2's range
    if(start1 <= start2 and end1 >= end2):
        contains = contains + 1
    # check if elf 2's range contains elf 1's range
    elif(start2 <= start1 and end2 >= end1):
        contains = contains + 1

print(contains)