# import modules
from collections import Counter

# read input file
with open('adventofcode2022/day6/day6input.txt', 'r') as file:
    for line in file:
        datastream = line.strip()

# find marker with 4 unique characters
for i in range(3, len(datastream)-3):
    # check character frequency in marker
    marker = datastream[i-4:i]
    freq = Counter(marker)
    
    # print first marker with 4 unique characters
    if(len(freq) == 4):
        print(i)
        break