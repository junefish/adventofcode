contents = []
with open('/data/data/com.termux/files/home/adventofcode/adventofcode2022/day3/day3example.txt', 'r') as input:
    for line in input:
        package = line.strip()
        first_half, second_half = package[:len(package)//2], package[len(package)//2:]
        contents.append([first_half,second_half])

print(contents)
