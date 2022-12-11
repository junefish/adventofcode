movements = []
# read input file
with open('adventofcode2022/day9/day9example.txt', 'r') as file:
    for line in file:
        dir, dist = line.strip().split()
        movements.append((dir,int(dist)))
# print(movements)

# define H as bottom left corner of grid
H = {'x': 0, 'y': 0}

for move in movements:
    dir,dist = move
    
    # move left
    if(dir == 'L'):
        H['x'] -= dist
        
    # move right
    elif(dir == 'R'):
        H['x'] += dist
    
    # move up
    elif(dir == 'U'):
        H['y'] += dist
    
    # move down
    elif(dir == 'D'):
        H['y'] -= dist
    
    print(H['x'],H['y'])