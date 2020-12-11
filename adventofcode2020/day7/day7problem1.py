with open(r'adventofcode2020\day7\day7input.txt', 'r') as input:
    rules = [line.rstrip() for line in input]

bag_rules = {}
parent_bags = []
total_ancestors = set()
for rule in rules:
    words = rule.split(' ')
    color = words[0] + ' ' + words[1]
    contents = ' '.join([str(word) for word in words[4:]]) 
    bag_rules.update({color : contents})

    if('shiny gold' in contents):
        parent_bags.append(color)
total_ancestors.update(parent_bags)

temp = []
for parent in parent_bags:
    for rule in rules:
        words = rule.split(' ')
        color = words[0] + ' ' + words[1]
        contents = ' '.join([str(word) for word in words[4:]]) 
        
        if('shiny gold' in contents):
            temp.append(color)

while(len(parent_bags) > 0):
    parent_bags = temp
    total_ancestors.update(parent_bags)
    temp = []
    for parent in parent_bags:
        for rule in rules:
            words = rule.split(' ')
            color = words[0] + ' ' + words[1]
            contents = ' '.join([str(word) for word in words[4:]]) 
            
            if('shiny gold' in contents):
                temp.append(color)
print(len(total_ancestors))