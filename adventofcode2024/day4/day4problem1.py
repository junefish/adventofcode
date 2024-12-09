word_search = []
with open("adventofcode2024/day4/day4example.txt", "r") as input:
    for line in input:
        word_search.append(line.strip())
# print(word_search)

word = "XMAS"

height = len(word_search)
width = len(word_search[0])


def count(grid, i, j):
    if grid[i][j] != word[0]:
        return 0
    return sum(
        [
            j > 3 and grid[i][j : j - 4 : -1] == word,  # left
            j == 3 and grid[i][j::-1] == word,  # left at edge
            j < width - 3 and grid[i][j : j + 4] == word,  # right
            i > 2 and "".join(grid[i - n][j] for n in range(4)) == word,  # up
            i < height - 3
            and "".join(grid[i + n][j] for n in range(4)) == word,  # down
            i > 2
            and j < width - 3
            and "".join(grid[i - n][j + n] for n in range(4)) == word,  # quad-I
            i > 2
            and j > 2
            and "".join(grid[i - n][j - n] for n in range(4)) == word,  # quad-II
            i < height - 3
            and j > 2
            and "".join(grid[i + n][j - n] for n in range(4)) == word,  # quad-III
            i < height - 3
            and j < width - 3
            and "".join(grid[i + n][j + n] for n in range(4)) == word,  # quad-IV
        ]
    )


result = 0
for i in range(height):
    for j in range(width):
        result += count(word_search, i, j)
print(result)
