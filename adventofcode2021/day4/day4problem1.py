with open('adventofcode2021\day4\day4example.txt', 'r') as input:
  called, *boards = input.read().split('\n\n')
  called = [int(i) for i in called.split(',')]
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

def check_winner(board):
    winner = False

    for row in board:
        winner = all(elem in ['x'] for elem in row)

        if winner:
            return winner

temp_board = [['x', 'x', 'x', 'x', 'x'], [0, 1, 2, 4, 5], [0, 1, 2, 4, 5], [0, 1, 2, 4, 5], [0, 1, 2, 4, 5]]
print(check_winner(temp_board))