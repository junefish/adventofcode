jets = []
with open('adventofcode2022/day17/day17example.txt') as input:
    for line in input:
        for char in line:
            jets.append(char)
# print(jets)

rocks = []
"""
first rock:
    #### 
"""
rocks.append([(0,0),(0,1),(0,2),(0,3)])
"""
second rock
    .#.
    ###
    .#.
"""
rocks.append([(0,1),(1,0),(1,1),(1,2),(2,1)])
"""
third rock
    ..#
    ..#
    ###
"""
rocks.append([(0,0),(0,1),(0,2),(1,2),(2,2)])
"""
fourth rock:
    #
    #
    #
    #
"""
rocks.append([(0,0),(1,0),(2,0),(3,0)])
"""
fifth rock:
    ##
    ##
"""
rocks.append([(0,0),(1,0),(1,0),(1,1)])
print(rocks)