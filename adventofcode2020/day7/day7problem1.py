with open('adventofcode2020\day7\day7input.txt', 'r') as input:
    rules = [line.rstrip() for line in input]

bag_colors = {}
parent_bags = []
for rule in rules:
    words = rule.split(' ')
    color = words[0] + ' ' + words[1]
    contents = ' '.join([str(word) for word in words[4:]]) 
    bag_colors.update({color : contents})

    if('shiny gold' in contents):
        parent_bags.append(color)
        
# for parent in parent_bags:
#     if(parent in contents)
