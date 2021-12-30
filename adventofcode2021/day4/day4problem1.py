with open('adventofcode2021\day4\day4example.txt', 'r') as input:
  called, *boards = input.read().split('\n\n')
#  boards = [list(board) for board in boards]
  boards = [[[int(col) for col in row.split()] for row in board.split('\n')] for board in boards]

def mark_boards(number, board):
    for row in board:
        for col in range(0, len(row)):
            if(row[col] == number):
                row[col] = 'x'

def sum_boards(board):
    sum = 0
    for row in board:
        for entry in row:
            if entry != 'x':
                sum += entry
    return sum

mark_boards(called[0], boards[0])
print(sum_boards(boards[0]))

temp_sum = 0
for row in boards[0]:
    for num in row:
        temp_sum += num

print(temp_sum)