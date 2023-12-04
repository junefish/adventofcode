#!/usr/bin/python

with open("day2input.txt", "r") as file:
    input = file.read()
    intcode = map(int, input.split(","))


def alarm(intcode):
    intcode[1] = 12
    intcode[2] = 2


def opcode(intcode):
    for i in range(0, len(intcode) - 1, 4):
        pos1 = intcode[i]
        pos2 = intcode[i + 1]
        pos3 = intcode[i + 2]
        pos4 = intcode[i + 3]

        if pos1 == 1:
            intcode[pos4] = intcode[pos2] + intcode[pos3]
        elif pos1 == 2:
            intcode[pos4] = intcode[pos2] * intcode[pos3]
        elif pos1 == 99:
            break
    return intcode


alarm(intcode)
print("The full altered intcode is:\n" + str(opcode(intcode)))
