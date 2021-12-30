with open('adventofcode2021\day4\day4example.txt', 'r') as input:
  called, *boards = input.read().split('\n\n')
#  boards = [list(board) for board in boards]
  boards = [[[int(col) for col in row.split()] for row in board.split('\n')] for board in boards]