valid_passwords = 0

with open('adventofcode2020\day2\day2input.txt', 'r') as input:
  for line in input:
    policy, password = line.split(':')
    
    char = policy[-1]
    min, max = map(int, policy[:-2].split('-'))

    if password.count(char) in range(min, max + 1):
       valid_passwords += 1
  print(valid_passwords)