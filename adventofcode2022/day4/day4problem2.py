assignments = []
with open('adventofcode2022/day4/day4example.txt', 'r') as input:
    for line in input:
        line = line.strip()
        assignments.append(line.split(','))
 
contains = 0
for pair in assignments:
    elf1,elf2 = pair[0],pair[-1]    
    start1,end1 = elf1.split('-')
    start2,end2 = elf2.split('-')
    
    # cast to integer
    start1 = int(start1)
    start2 = int(start2)
    end1 = int(end1)
    end2 = int(end2)