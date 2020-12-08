with open('adventofcode2020\day7\day7input.txt', 'r') as input:
    rules = [line.rstrip() for line in input]

bag_colors = {}
for rule in rules:
    words = rule.split(' ')
    color = words[0] + ' ' + words[1]
    contents = ' '.join([str(word) for word in words[4:]]) 
    bag_colors.update({color : contents})