#!/usr/bin/python

with open('day2input.txt', 'r') as file:
    input = file.read()
    intcode = input.split(',')

for i in range(0,3):
    print(intcode[i])
