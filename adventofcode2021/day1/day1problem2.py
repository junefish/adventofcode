depths = []

with open('adventofcode2021\day1\day1input.txt', 'r') as input:
  for line in input:
    item = line.split('\n')
    depths.append(int(item[0]))

window_sums = []
for i in range(0, len(depths)-2):
    window = (depths[i], depths[i+1], depths[i+2])
    window_sums.append(sum(window))
# print(window_sums)

deltas = []
for i in range(0, len(window_sums)):
    if(i == 0):
        delta = "N/A - no previous measurement"
    elif(window_sums[i] > window_sums[i-1]):
        delta = "increased"
    elif(window_sums[i] < window_sums[i-1]):
        delta = "decreased"
    deltas.append(delta)
 #   print((str(window_sums[i])) + delta)

print(deltas.count("increased"))