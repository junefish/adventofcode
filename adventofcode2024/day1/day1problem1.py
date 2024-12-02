left = []
right = []

with open("adventofcode2024/day1/day1example.txt", "r") as input:
    for line in input:
        left.append(int(line.strip().split(" ")[0]))
        right.append(int(line.strip().split(" ")[-1]))


def find_distance(list1, list2):
    if len(list1) != len(list2):
        result = "Lists are not the same length"
    else:
        result = []
        for i in range(len(list1)):
            result.append(abs(list1[i] - list2[i]))
    return result


distances = find_distance(sorted(left), sorted(right))

print(sum(distances))
