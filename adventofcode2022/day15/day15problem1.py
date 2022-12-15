sensors = []
beacons = []
with open('adventofcode2022/day15/day15input.txt', 'r') as input:
    for line in input:
        s = line.split(': ')[0]
        b = line.split(': ')[1]
        sensors.append(s.strip())
        beacons.append(b.strip())
        
# print(sensors)
# print(beacons)

for sensor in sensors:
    sensors.remove(sensor)
    s = sensor.replace('Sensor at ', '')
    sensors.append(s)

sensors = [item for item in sensors if not item.startswith('S')]
# print(sensors)

for beacon in beacons:
    beacons.remove(beacon)
    b = beacon.replace('closest beacon is at ', '')
    beacons.append(b)

beacons = [item for item in beacons if not item.startswith('c')]
# print(beacons)

positions = []
for i,_ in enumerate(sensors):
    line = {}
    s = sensors[i].split(', ')
    line['Sx'] = int(s[0].replace('x=', ''))
    line['Sy'] = int(s[1].replace('y=', ''))
    
    b = beacons[i].split(', ')
    line['Bx'] = int(b[0].replace('x=', ''))
    line['By'] = int(b[1].replace('y=', ''))
    
    positions.append(line)
print(positions)