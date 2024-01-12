#!/usr/bin/python


def calcFuel(mass):
    fuel = round(mass / 3) - 2
    return int(fuel)


sum = 0
with open("day1input.txt", "r") as input:
    for line in input:
        sum += calcFuel(int(line))

print("Test values:")
print(calcFuel(12))
print(calcFuel(14))
print(calcFuel(1969))
print(calcFuel(100756))

print("Puzzle answer: " + str(sum))
