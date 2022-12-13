movements = []
# read input file
with open('adventofcode2022/day9/day9example.txt', 'r') as file:
    for line in file:
        dir, dist = line.strip().split()
        movements.append((dir,int(dist)))
# print(movements)

# define H as bottom left corner of grid
H = {'x': 0, 'y': 0}
# define tail as overlapping with head at start
T = {'x': 0, 'y': 0}
Tx = T['x']
Ty = T['y']

H_positions = []
T_stops = []
T_positions = []

for move in movements:
    dir,dist = move
    
    # move left
    if(dir == 'L'):
        Hx = H['x'] - dist
        Hy = H['y']
        a = -1
        
    # move right
    if(dir == 'R'):
        Hx = H['x'] + dist
        Hy = H['y']
        a = 1
        
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
    if(dir == 'U'):
        Hx = H['x']
        Hy = H['y'] + dist
        a = 1
    
    # move down
    if(dir == 'D'):
        Hx = H['x']
        Hy = H['y'] - dist
        a = -1
    
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
    H_positions.append((H['x'],H['y']))
    
    # check if tail is close to the head
    # a = int(abs(dist)/dist)
    if(abs(Hx-Tx) > 1):
        if(Ty != Hy): 
            Ty = Hy
        Tx += a
        
    if(abs(Hy-Ty) > 1):
        if(Tx != Hx):
            Tx = Hx
        Ty += a
    
    T_stops.append((Tx,Ty))
    
# print(H_positions)
# print(T_stops)

for i in range(len(T_stops)-1):
    Tx = T_stops[i][0]
    Ty = T_stops[i][1]
    
    # increment T stepwise when moving L/R
    if(abs(T_stops[i+1][1] - T_stops[i][1]) < 1):
        while(abs(T_stops[i+1][0] - T_stops[i][0]) > 1):
            T_positions.append((Tx,Ty))
            # increase by 1 if moving R
            if(T_stops[i+1][0] > T_stops[i][0]):
                Tx += 1
            # decrease by 1 if moving L
            if(T_stops[i+1][0] < T_stops[i][0]):
                Tx -= 1
    # increment T stepwise when moving L/R
    if(abs(T_stops[i+1][0] - T_stops[i][0]) < 1):
        while(abs(T_stops[i+1][1] - T_stops[i][1]) > 1):
            T_positions.append((Tx,Ty))
            # increase by 1 if moving U
            if(T_stops[i+1][1] > T_stops[i][1]):
                Ty += 1
            # decrease by 1 if moving L
            if(T_stops[i+1][1] < T_stops[i][1]):
                Ty -= 1
    T_positions.append((Tx,Ty))
print(T_positions)