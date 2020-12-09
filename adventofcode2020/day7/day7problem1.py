with open('adventofcode2020\day7\day7input.txt', 'r') as input:
    rules = [line.rstrip() for line in input]

bag_rules = {}
parent_bags = set()
for rule in rules:
    words = rule.split(' ')
    color = words[0] + ' ' + words[1]
    contents = ' '.join([str(word) for word in words[4:]]) 
    bag_rules.update({color : contents})

    if('shiny gold' in contents):
        parent_bags.add(color)

temp = []
for item in bag_rules.items():
    for parent in parent_bags:
        if(parent in item[1]):
            temp.append(item[0])
parent_bags.update(temp)

print(len(parent_bags))