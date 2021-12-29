fish_timers = []
with open('adventofcode2021\day6\day6input.txt', 'r') as input:
  for line in input:
    item = line.split('\n')
    fish_timers = item[0].split(',')

fish_timers = list(map(int, fish_timers))

day = 1
while(day <= 80):
    for i in range(0, len(fish_timers)):
        timer = fish_timers[i]
        if(timer == 0):
            fish = 6
            fish_timers.append(8)
        else:
            fish = timer - 1
        fish_timers[i] = fish

    day += 1
print(len(fish_timers))