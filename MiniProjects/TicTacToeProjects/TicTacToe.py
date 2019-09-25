#Python Tic Tac Toe

board =["  " for i in range(9)]

def print_board():
    #could do this in for loop
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row1 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row1 = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
