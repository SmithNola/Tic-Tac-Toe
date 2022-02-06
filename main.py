# Create board
def new_board():
    empty_board = [['N', 'N', 'N'], ['N', 'N', 'N'], ['N', 'N', 'N']]
    return empty_board


def print_board(board):
    print("\t0\t1\t2")
    row = 0
    for i in board:
        print("{}{}".format(row, i))
        row += 1

#  Check if player inserted correct coordinate
def valid_move(board, x, y):
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Invalid Move: Enter an integer")
        return False
    if int(x) > 2 or int(x) < 0 or int(y) > 2 or int(y) < 0:
        print("Invalid Move: Coordinates out of range")
        return False
    if board[int(x)][int(y)] != 'N':
        print("Invalid Move: Spot taken")
        return False
    return True


# Take user input for turns
def get_move():
    x = input("What is the x coordinate?")
    y = input("What is the y coordinate?")
    while not valid_move(board, x, y):
        x = input("What is the x coordinate?")
        y = input("What is the y coordinate?")
    print(x, y)
    return int(x), int(y)

#  edits board based on player movement
def make_move(board, player, move_coord):
    if player == 0:
        sign = 'O'
    else:
        sign = 'X'
    board[move_coord[0]][move_coord[1]] = sign
    return board


# Declare winner
def get_winner(board):
    if len(set(board[0])) == 1 and board[0][0] != 'N':  # first row win
        return True, board[0][0]
    elif len(set(board[1])) == 1 and board[1][0] != 'N':  # second row win
        return True, board[1][0]
    elif len(set(board[2])) == 1 and board[2][0] != 'N':  # third row win
        return True, board[2][0]
    elif len(set([board[0][0], board[1][1], board[2][2]])) == 1 and board[0][0] != 'N':  # right diagonal row win
        return True, board[0][0]
    elif len(set([board[2][0], board[1][1], board[0][2]])) == 1 and board[2][0] != 'N':  # left diagonal row win
        return True, board[2][0]
    elif len(set([board[0][0], board[1][0], board[2][0]])) == 1 and board[2][0] != 'N':  # first column win
        return True, board[2][0]
    elif len(set([board[0][1], board[1][1], board[2][1]])) == 1 and board[0][1] != 'N':  # second column win
        print(all([board[0][1], board[1][1], board[2][1]]))
        return True, board[0][1]
    elif len(set([board[0][2], board[1][2], board[2][2]])) == 1 and board[0][2] != 'N':  # third column win
        return True, board[0][2]
    else:
        return False, None


# Play game
board = new_board()
winner = False, None
turn = 1
print('X goes first')
while winner[0] == False:
    if turn < 10:
        move_coord = get_move()
        board = make_move(board, turn % 2, move_coord)
        print_board(board)
        winner = get_winner(board)
        turn += 1
    else:
        winner = True, "Draw"
print("The winner is " + winner[1])
