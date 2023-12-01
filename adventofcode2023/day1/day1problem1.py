calibrations = []

# read input file
with open('adventofcode2023/day1/day1input.txt', 'r') as input:
    for line in input:
        tmp = ""
        for char in line.strip():
            if(char.isnumeric()):
                tmp += char
        if(len(tmp) == 2):
            calibrations.append(int(tmp))
        elif(len(tmp) == 1):
            calibrations.append(int(tmp+tmp))
        elif(len(tmp) > 2):
            calibrations.append(int(tmp[0] + tmp[-1]))

print(sum(calibrations))