calibrations = []

# read input file
with open('adventofcode2023/day1/day1example.txt', 'r') as input:
    for line in input:
        tmp = ""
        for char in line.strip():
            if(char.isnumeric()):
                tmp += char
        calibrations.append(tmp)
        
print(calibrations)