paths = []
with open('adventofcode2022/day14/day14example.txt') as input:
    for line in input:
        tmp = line.strip().split(' -> ')
        tmp2 = []
        for elem in tmp:
            point = (int(elem.split(',')[0]), int(elem.split(',')[1]))
            tmp2.append(point)
        paths.append(tmp2)
print(paths)