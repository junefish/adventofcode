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
print(sensors)