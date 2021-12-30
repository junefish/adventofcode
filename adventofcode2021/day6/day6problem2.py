from typing import DefaultDict


fish_timers = []
with open('adventofcode2021\day6\day6input.txt', 'r') as input:
  for line in input:
    item = line.split('\n')
    fish_timers = item[0].split(',')

fish_timers = list(map(int, fish_timers))
fish_map = {}
for fish in fish_timers:
    if fish not in fish_map:
        fish_map[fish] = 0
    fish_map[fish] += 1

day = 1
while(day <= 256):
    updated_map = DefaultDict(int)

    for fish, count in fish_map.items():
        if fish == 0:
            updated_map[6] += count
            updated_map[8] += count
        else:
            updated_map[fish - 1] += count

        fish_map = updated_map

    day += 1
print(sum(fish_map.values()))