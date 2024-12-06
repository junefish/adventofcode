word_search = []
with open("adventofcode2024/day4/day4example.txt", "r") as input:
    for line in input:
        word_search.append(list(line.strip()))
# print(word_search)

word = "XMAS"

height = len(word_search)
width = len(word_search[0])


def find_substring(grid, i, j):
    if grid[i][j] != "X":
        str = ""
    elif j > 2:  # left
        str = grid[i][j : j - 4 : -1]
    elif j < width - 3:  # right
        str = grid[i][j : j + 4]
    elif i > 2:  # up
        str = "".join(grid[i - n][j] for n in range(4))
    elif i < height - 3:  # down
        str = "".join(grid[i + n][j] for n in range(4))
    elif i > 2 and j < width - 3:  # quad-I
        str = "".join(grid[i - n][j + n] for n in range(4))
    elif i > 2 and j > 2:  # quad-II
        str = "".join(grid[i - n][j - n] for n in range(4))
    elif i < height - 3 and j > 2:  # quad-III
        str = "".join(grid[i + n][j - n] for n in range(4))
    elif i < height - 3 and j < width - 3:  # quad-IV
        str = "".join(grid[i + n][j + n] for n in range(4))

    return str
