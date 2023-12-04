valves = []
with open("adventofcode2022/day16/day16example.txt") as input:
    for line in input:
        a = line.strip().split(";")
        b = a[0].split(" ")
        c = a[1].split(" ")

        valve = b[1]
        flow = int(b[4].split("=")[-1])

        x = []
        x.extend([valve, flow])

        for i in range(5):
            c.pop(0)
        x.extend(c)

        valves.append(x)
print(valves)
