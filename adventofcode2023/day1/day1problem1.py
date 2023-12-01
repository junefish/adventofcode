calibrations = []

# read input file
with open('adventofcode2023/day1/day1example.txt', 'r') as input:
    for line in input:
        calibrations.append(line.strip())
        
print(calibrations)