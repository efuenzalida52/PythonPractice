#Python Tic Tac Toe

board =[" " for i in range(9)]
def print_board():
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

#could do this in for loop
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

#player move section
def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    print("Player {}'s turn!".format(number))
    
    choice= int(input("Place your 'x' or 'o' by entering (1-9): ").strip())
    if board[choice -1] == " ":     #-1 from player choice due to indexing
        board[choice -1] = icon
    else:
        print()
        print("Sorry, that space is taken!")
        # need to implement players turn not being skipped


#determine when a player wins
def victory(icon):
     if (board[0]==icon and board[1]==icon and board[2]==icon)or\
        (board[3]==icon and board[4]==icon and board[5]==icon)or\
        (board[6]==icon and board[7]==icon and board[8]==icon)or\
        (board[0]==icon and board[3]==icon and board[6]==icon)or\
        (board[1]==icon and board[4]==icon and board[7]==icon)or\
        (board[2]==icon and board[5]==icon and board[8]==icon)or\
        (board[0]==icon and board[4]==icon and board[8]==icon)or\
        (board[2]==icon and board[4]==icon and board[6]==icon):
        return True
     else:
        return False

#determine when there is a tie
def draw():
    if "  " not in board:
        return True
    else:
        return False
        
while True:
    print_board()
    player_move("X")
    print_board()
    if victory("X"):
        print("X wins!")
        break
    elif draw():
        print("Draw!")
    player_move("O")
    if victory("O"):
        print_board()
        print("O wins!")
        break
    elif draw():
        print("Draw!")
        break
