with open("adventofcode2020\day3\day3input.txt", "r") as input:
    hilltop = [line.rstrip() for line in input]

    i = 0
    trees = 0
    for x in hilltop:
        l = len(x)
        if i >= l:
            i -= l
        if x[i] == "#":
            trees += 1
        i += 3

print(trees)
