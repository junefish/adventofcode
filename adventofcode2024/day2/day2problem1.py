reports = []
with open("adventofcode2024/day2/day2example.txt", "r") as input:
    for line in input:
        reports.append([int(item) for item in line.strip().split(" ")])

print(reports)


def check_safety(list):
    # check adjacent levels difference
    if all(abs(list[i] - list[i + 1]) in range(1, 4) for i in range(len(list) - 1)):
        # check if strictly increasing
        if all(list[i] < list[i + 1] for i in range(len(list) - 1)):
            return True
        # check if strictly decreasing
        if all(list[i] > list[i + 1] for i in range(len(list) - 1)):
            return True
    return False


for level in reports:
    print(check_safety(level))
