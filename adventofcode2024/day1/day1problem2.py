left = []
right = []

with open("adventofcode2024/day1/day1example.txt", "r") as input:
    for line in input:
        left.append(int(line.strip().split(" ")[0]))
        right.append(int(line.strip().split(" ")[-1]))


def similarity_score(list1, list2):
    scores = []
    for item in list1:
        count = list2.count(item)
        scores.append(item * count)
    return scores


print(similarity_score(left, right))
