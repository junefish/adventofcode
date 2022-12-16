input = []
with open('adventofcode2022/day12/day12input.txt', 'r') as file:
    for line in file:
        x = [*line.strip()]
        input.append(x)
# print(input)

def findCoords(map):
    for i,_ in enumerate(map):
        for j,_ in enumerate(map[0]):
            if(map[i][j] == 'S'):
                start = (i,j)
            if(map[i][j] == 'E'):
                end = (i,j)
    return start, end
start, end = findCoords(input)
# print(start, end)

# replace start with 'a' and end with 'z' for unicode parsing later
heightmap = []
for line in input:
    row = list(map(lambda item: item.replace('S','a'), line))
    row2 = list(map(lambda item: item.replace('E','z'), row))
    heightmap.append(row2)
# print(heightmap)
    
# find adjacent points
def findNeighbors(map, point):
    x_min,y_min = 0,0
    x_max = len(map) - 1
    y_max = len(map[0]) - 1
    x, y = point

    # -2 allowing only single steps down the mountain
    node_height = ord(map[x][y]) - 2

    neighbors = []

    # ensure X isn't an edge and left isn't lower than - 1 height
    if (x_min < x) and (node_height < ord(map[x - 1][y])):
        neighbors.append((x - 1, y))

    # same for right
    if (x < x_max) and (node_height < ord(map[x + 1][y])):
        neighbors.append((x + 1, y))

    # same for top
    if (y_min < y) and (node_height < ord(map[x][y - 1])):
        neighbors.append((x, y - 1))

    # same for bottom
    if (y < y_max) and (node_height < ord(map[x][y + 1])):
        neighbors.append((x, y + 1))
        
    return(neighbors)

def search(map,end):
    mountains = [end]
    level = {}
    level[end] = 0
    
    while mountains:
        current = mountains.pop(0)
        for neighbor in findNeighbors(map, current):
            if neighbor not in level:
                level[neighbor] = level[current] + 1
                mountains.append(neighbor)

    return level

print(search(heightmap,end)[start])