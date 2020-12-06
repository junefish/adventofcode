valid_passwords = 0

with open('adventofcode2020\day2\day2input.txt', 'r') as input:
  for line in input:
    policy, password = line.split(':')
    
    char = policy[-1]
    pos1, pos2 = map(int, policy[:-2].split('-'))

    a = bool(password[pos1] == char)
    b = bool(password[pos2] == char)

    if (a and not b) or (b and not a):
        valid_passwords += 1
  print(valid_passwords)