# ToDo

# Create board
def new_board():
    empty_board = [['N', 'N', 'N'], ['N', 'N', 'N'], ['N', 'N', 'N']]
    return empty_board

def print_board(board):
    print("\t1\t2\t3")
    row = 0
    for i in board:
        print("{}{}".format(row,i))
        row+=1


board = new_board()
# Take user input for turns

# Play game

# Declare winner
print_board(board)