#!/usr/bin/python

with open('day2input.txt', 'r') as file:
    input = file.read()
    intcode = map(int,input.split(','))

def opcode(intcode):
    for i in range(0,len(intcode)-1,4):
        pos1 = intcode[i]
        pos2 = intcode[i+1]
        pos3 = intcode[i+2]
        pos4 = intcode[i+3]

        if(pos1 == 1):
            intcode[pos4] = intcode[pos2] + intcode[pos3]
        elif(pos1 == 2):
            intcode[pos4] = intcode[pos2] * intcode[pos3]
        elif(pos1 == 99):
            break
    return intcode

def testWords(intcode):
    for noun in range(100):
        for verb in range(100):
            test_code = list(intcode)

            test_code[1] = noun
            test_code[2] = verb

            if(opcode(test_code)[0] == 19690720):
                return 100 * noun + verb
                break
#            else:
#                return ["no results","were found]

print(testWords(intcode))
