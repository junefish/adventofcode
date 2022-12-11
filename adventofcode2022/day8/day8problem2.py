forest = []

with open('adventofcode2022/day8/day8example.txt', 'r') as file:
    for line in file:
        treeline = (line.strip())
        forest.append([*treeline])
    forest = [list(map(int, x)) for x in forest]
    
    # transpose forest for easier parsing
    forest2 = list(zip(*forest))

scores = []
for i in range(len(forest[0])):
    for j in range(len(forest)):
        tree = forest[i][j]
        
        left = 0
        for t in forest[i][0:j][::-1]:
            left += 1
            if t >= tree:
                break
        
        right = 0
        for t in forest[i][j+1:]:
            right += 1
            if t >= tree:
                break

        up = 0
        for t in forest2[j][0:i][::-1]:
            up += 1
            if t >= tree:
                break
            
        down = 0
        for t in forest2[j][i+1:]:
            down += 1
            if t >= tree:
                break
        
        # calculate scenic score
        scores.append(left * right * up * down)

print(max(scores))