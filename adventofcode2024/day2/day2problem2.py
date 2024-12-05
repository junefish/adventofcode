reports = []
with open("adventofcode2024/day2/day2example.txt", "r") as input:
    for line in input:
        reports.append([int(item) for item in line.strip().split(" ")])


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


safe_reports = 0
unsafe_reports = []
for report in reports:
    if check_safety(report):
        safe_reports += 1
    else:
        unsafe_reports.append(report)


def permutations(report):
    removed_levels = []
    for i in range(len(report)):
        result = []
        for j in range(len(report)):
            if i != j:
                result.append(report[j])
        removed_levels.append(result)
    return removed_levels


for report in unsafe_reports:
    if any(check_safety(x) for x in permutations(report)):
        safe_reports += 1
print(safe_reports)
