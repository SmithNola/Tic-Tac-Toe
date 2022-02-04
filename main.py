# ToDo

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
    print(x,y)
    return int(x), int(y)


def make_move(board, player, move_coord):
    if player == 1:
        sign = 'O'
    if player == 2:
        sign = 'X'
    board[move_coord[0]][move_coord[1]] = sign
    return board


# Play game
board = new_board()
move_coord = get_move()
board = make_move(board, 1, move_coord)
print_board(board)


# Declare winner
