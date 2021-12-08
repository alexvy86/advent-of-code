import sys

boards = []

with open('day4.input') as f:
    numbers = [int(num) for num in f.readline().split(',')]

    f.readline()

    b = []
    for line in f.read().splitlines():
        if len(line) == 0:
            boards.append(b)
            b = []
        else:
            b.append([int(num) for num in line.split()])

def board_won(board): # pylint: disable=missing-function-docstring
    transpose_board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    return any(all(cell == -1 for cell in row) for row in board) \
        or any(all(cell == -1 for cell in row) for row in transpose_board)

def calculate_winning_score(winning_board, winning_number): # pylint: disable=missing-function-docstring
    return sum(cell for row in winning_board for cell in row if cell != -1) * winning_number

for n in numbers:
    for board_num, board in enumerate(boards):
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == n:
                    board[i][j] = -1
                    if board_won(board):
                        print(calculate_winning_score(board, n))
                        sys.exit()
