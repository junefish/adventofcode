fish_timers = []
with open('adventofcode2021\day6\day6example.txt', 'r') as input:
  for line in input:
    item = line.split('\n')
    fish_timers = item[0].split(',')

fish_timers = list(map(int, fish_timers))