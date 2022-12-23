input = []
map = []
path = []
with open('adventofcode2022/day22/day22example.txt') as file:
    for line in file:
        input.append(line.strip())
    
    m = input[0:-2]
    for row in m:
        map.append([char for char in row])
    
    p = input[-1]
    q = [[]]
    for char in p:
        if not char.isnumeric():
            q.extend([[char],[]])
        else:
            q[-1].append(char)
    for item in q:
        if item[0].isnumeric():
            path.append(eval("".join(item)))
        else:
            path.append(item[0])
print(map)
print(path)