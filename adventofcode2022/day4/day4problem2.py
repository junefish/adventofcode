# initialise list
assignments = []

# read input file
with open("adventofcode2022/day4/day4input.txt", "r") as input:
    for line in input:
        line = line.strip()
        assignments.append(line.split(","))

# calculate overlapping pairs
contains = 0
for pair in assignments:
    elf1, elf2 = pair[0], pair[-1]
    start1, end1 = elf1.split("-")
    start2, end2 = elf2.split("-")

    # cast to integer
    start1 = int(start1)
    start2 = int(start2)
    end1 = int(end1)
    end2 = int(end2)

    # check if elf1's range overlaps before elf 2's range
    if start1 <= start2 and end1 >= start2:
        contains = contains + 1
    # check if elf2's range overlaps before elf 1's range
    elif start2 <= start1 and end2 >= start1:
        contains = contains + 1

# print answer
print(contains)
