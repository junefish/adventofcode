received = []
with open('adventofcode2022/day13/day13example.txt', 'r') as input:
    for line in input:
        received.append(line.strip())
# print(received)

packets = [[]]
delimiter = ''
for line in received:
    if line == delimiter:
        packets.append([])
    elif line != delimiter: 
        packets[-1].append(line.strip('[').strip(']').split(','))
print(packets[0])