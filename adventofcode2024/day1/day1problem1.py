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
        for i in range(len(list1)):
            print(
                str(list1[i])
                + " - "
                + str(list2[i])
                + " = "
                + str(abs(list1[i] - list2[i]))
            )


find_distance(sorted(left), sorted(right))
