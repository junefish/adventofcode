blueprints = []
with open("adventofcode2022/day19/day19example.txt") as input:
    for line in input:
        label = (line.strip().split(": "))[0].split(" ")
        number = int(label[-1])

        list = []
        robots = (line.strip().split(": "))[-1].split(". ")
        for bot in robots:
            info = []
            type = bot.split(" ")[1]

            info.append(type)
            if bot.split(" ")[-3] == "and":
                cost_num1 = int(bot.split(" ")[4])
                cost_type1 = bot.split(" ")[5].strip(".")
                cost1 = {cost_type1: cost_num1}

                info.append(cost1)

                cost_num2 = int(bot.split(" ")[-2])
                cost_type2 = bot.split(" ")[-1].strip(".")
                cost2 = {cost_type2: cost_num2}

                info.append(cost2)
            else:
                cost_num = int(bot.split(" ")[4])
                cost_type = bot.split(" ")[5].strip(".")
                cost = {cost_type: cost_num}

                info.append(cost)
            list.append(info)

        blueprints.append({number: info})
print(blueprints)
