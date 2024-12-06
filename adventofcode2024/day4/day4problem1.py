word_search = []
with open("adventofcode2024/day4/day4example.txt", "r") as input:
    for line in input:
        word_search.append(list(line.strip()))
# print(word_search)

word = "XMAS"

height = len(word_search)
width = len(word_search[0])
