# import modules
from collections import Counter

# read input file
with open("adventofcode2022/day6/day6input.txt", "r") as file:
    for line in file:
        datastream = line.strip()

# find marker with 4 unique characters
for i in range(14, len(datastream)):
    marker = datastream[i - 14 : i]
    freq = Counter(marker)

    # print first marker with 4 unique characters
    if len(freq) == 14:
        print(i)
        break
