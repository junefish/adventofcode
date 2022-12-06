from collections import Counter

with open('adventofcode2022/day6/day6example.txt', 'r') as file:
    for line in file:
        datastream = line.strip()
        
# print(datastream)

for i in range(3, len(datastream)-3):
    marker = datastream[i-4:i]
    freq = Counter(marker)
    
    if(len(freq) == 4):
        print(i)
        break