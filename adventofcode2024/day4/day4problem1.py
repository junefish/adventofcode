word_search = []
with open("adventofcode2024/day4/day4example.txt", "r") as input:
    for line in input:
        word_search.append(list(line.strip()))
# print(word_search)

word = "XMAS"

height = len(word_search)
width = len(word_search[0])


def count(grid, i, j):
    if grid[i][j] != "X":
        return 0
    return sum(
        [
            j > 2 and grid[i][j : j - 4 : -1] == "XMAS",  # left
            j < width - 3 and grid[i][j : j + 4] == "XMAS",  # right
            i > 2 and "".join(grid[i - n][j] for n in range(4)) == "XMAS",  # up
            i < height - 3
            and "".join(grid[i + n][j] for n in range(4)) == "XMAS",  # down
            i > 2
            and j > 2
            and "".join(grid[i - n][j - n] for n in range(4)) == "XMAS",  # left-up
            i > 2
            and j < width - 3
            and "".join(grid[i - n][j + n] for n in range(4)) == "XMAS",  # right-up
            i < height - 3
            and j > 2
            and "".join(grid[i + n][j - n] for n in range(4)) == "XMAS",  # left-down
            i < height - 3
            and j < width - 3
            and "".join(grid[i + n][j + n] for n in range(4)) == "XMAS",  # right-down
        ]
    )
