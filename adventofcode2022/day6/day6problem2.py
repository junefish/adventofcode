from collections import Counter

with open('adventofcode2022/day6/day6input.txt', 'r') as file:
    for line in file:
        datastream = line.strip()
        
for i in range(14, len(datastream)):
    marker = datastream[i-14:i]
    freq = Counter(marker)

    # print(marker, len(freq))
    
    if(len(freq) == 14):
        print(i)
        break