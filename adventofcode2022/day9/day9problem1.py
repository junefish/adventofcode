movements = []
# read input file
with open('adventofcode2022/day9/day9example.txt', 'r') as file:
    for line in file:
        dir, dist = line.strip().split()
        movements.append((dir,int(dist)))
# print(movements)

# define H as bottom left corner of grid
H = {'x': 0, 'y': 0}

H_positions = []
for move in movements:
    dir,dist = move
    
    # move left
    if(dir == 'L'):
        Hx = H['x'] - dist
        Hy = H['y']
        
    # move right
    elif(dir == 'R'):
        Hx = H['x'] + dist
        Hy = H['y']
        
    # increment H stepwise when moving L/R
    if(H['y'] == Hy):
        while(H['x'] != Hx):
            H_positions.append((H['x'],H['y']))
            # decrease by 1 if moving L
            if(H['x'] > Hx):
                H['x'] -= 1
            # increase by 1 if moving R
            if(H['x'] < Hx):
                H['x'] += 1
    
    # move up
    elif(dir == 'U'):
        Hx = H['x']
        Hy = H['y'] + dist
    
    # move down
    elif(dir == 'D'):
        Hx = H['x']
        Hy = H['y'] - dist
    
    # increment H stepwise when moving U/D
    if(H['x'] == Hx):
        while(H['y'] != Hy):
            H_positions.append((H['x'],H['y']))
            # increase by 1 if moving U
            if(H['y'] < Hy):
                H['y'] += 1
            # decrease by 1 if moving D
            if(H['y'] > Hy):
                H['y'] -= 1
print(H_positions)