with open('adventofcode2020\day3\day3input.txt', 'r') as input:
        hilltop = [line.rstrip() for line in input]

def treeCounter(right_slope, down_slope):
    x,y,trees = 0,0,0
    while y < len(hilltop):
        if(x >= len(hilltop[0])):
            x -= len(hilltop[0])
        if(hilltop[y][x] == '#'):
            trees += 1
        x += right_slope
        y += down_slope
    return(trees)

print(treeCounter(1,1) * treeCounter(3,1) * treeCounter(5,1) * treeCounter(7,1) *  treeCounter(1,2))