sensors = []
beacons = []
with open('adventofcode2022/day15/day15input.txt', 'r') as input:
    for line in input:
        s = line.split(': ')[0]
        b = line.split(': ')[1]
        sensors.append(s.strip())
        beacons.append(b.strip())
        
print(sensors)
print(beacons)