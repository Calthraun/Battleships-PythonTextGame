""" Based on lessons from codecademy.com """
""" Imports """
from random import randint #import randomizer for hiding ships

""" Initialize main variables """
board = []

""" Define main functions """
#formats and prints the board so it can be read.
def print_board(board):
    for row in board:
        print " ".join(row)

#generate random coordinates
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

""" Begin main program """
#generate 5x5 board
for x in range(5):
    board.append(["O"] * 5)

#display introduction and game board
print "Let's play Battleship!"
print_board(board)

#generate random ship coordinates
ship_row = random_row(board)
ship_col = random_col(board)

#display coordinates for debugging
#print ship_row
#print ship_col

#begin counting turns
for turn in range(4):
    #collect guess input
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    #check for hits
    if guess_row == ship_row and guess_col == ship_col:
        board[guess_row][guess_col] = "H"
        print_board(board)
        print "Congratulations! You sunk my battleship!"
        break
    
    #check for guesses out of range 
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        
        #check for conflicting guesses
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
            
        #check for miss
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            
        #display and increment turn number
        print "Turn", turn + 1
        
        #display updated board
        print_board(board)
        
        #check for game over
        if turn == 3:
            print "Game Over"

#give user a chance to read final output
raw_input("Press Enter to exit...")

