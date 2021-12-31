with open('adventofcode2021\day4\day4input.txt', 'r') as input:
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

    for col in range(0, len(board[0])):
        winner = all(elem in ['x'] for elem in [row[col] for row in board])

        if winner:
            return winner

    return winner

winner_found = False
while not winner_found:
    number = called[0]
    called = called[1:]

    for board in boards:
        mark_boards(number, board)
    
    index = 0
    while(index < len(boards)):
        if(check_winner(boards[index])):
            if(len(boards) > 1):
                boards.pop(index)
            
            else:
                winner_found = True
                print(sum_boards(boards[index]) * number)
                break
        
        else:
            index += 1