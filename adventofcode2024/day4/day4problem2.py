word_search = []
with open("adventofcode2024/day4/day4input.txt", "r") as input:
    for line in input:
        word_search.append(line.strip())
# print(word_search)

word = "MAS"

height = len(word_search)
width = len(word_search[0])

def count(grid, i, j):
    X = grid[i][j]
    if X != word[1]:
        return 0
    elif(i in range(1,height-1) and j in range(1,width-1)):
        if("".join([grid[i-1][j-1],X,grid[i+1][j+1]]) in [word,word[::-1]] and
                "".join([grid[i-1][j+1],X,grid[i+1][j-1]]) in [word,word[::-1]]):
                return 1
    return 0

result = 0
for i in range(height):
    for j in range(width):
        result += count(word_search, i, j)
print(result)