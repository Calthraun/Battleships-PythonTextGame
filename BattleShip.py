""" Based on lessons from codecademy.com """
""" Imports """
from random import randint #import randomizer for hiding ships
from os import system #import window naming function

""" Initialize Main Varibles """
play_again = "Y"

""" Define main functions """
#collects int input
def collect_int(message):
    int_var = 0
    while True:
        try:
            int_var = int(raw_input(message))
            break
        except ValueError:
            print "Oops, that's not a number, please try again."
    return int_var
            
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
#title window
system("title BATTLESHIPS")

while play_again == "Y":
    #clear board
    board = []
    
    #display introduction
    print "~BATTLESHIPS~"
    print "Destroy the enemy spy's submarine before he steals your secrets!"
    print "You have four missiles."
    print "Enter the coordinates you would like to fire at."
    print
    
    #generate 5x5 board
    for x in range(5):
        board.append(["O"] * 5)
    
    #display game board
    print_board(board)
    print
    
    #generate random ship coordinates
    ship_row = random_row(board)
    ship_col = random_col(board)
    
    #display coordinates for debugging
    #print ship_row + 1
    #print ship_col + 1
    #print
    
    #begin counting turns
    for turn in range(4):
        #display turn number
        print "Turn", turn + 1
        
        #collect guess input
        print "Enter two coordinates between 1 and 5."
        guess_row = collect_int("Enter guess Row:") - 1
        guess_col = collect_int("Enter guess Column:") - 1
        print
        
        #check for hits
        if guess_row == ship_row and guess_col == ship_col:
            #update board
            board[guess_row][guess_col] = "H"
            
            #display updated board
            print_board(board)
            print
            
            #display win message
            print "Congratulations! Your secrets are safe!"
            break
        
        #check for guesses out of range 
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                #display updated board
                print_board(board)
                print
                
                #display last turn result
                print "You missed the ocean! Aim more carefully next time."
                print
            
            #check for conflicting guesses
            elif(board[guess_row][guess_col] == "X"):
                #display updated board
                print_board(board)
                print
                
                #display last turn result
                print "You fired there already! He's still not there..."
                print
                
            #check for miss
            else:
                #update board
                board[guess_row][guess_col] = "X"
                
                #display updated board
                print_board(board)
                print
                
                #display last turn result
                print "Sploosh! You hit... some fish. Try again."
                print
                
            #check for game over
            if turn == 3:
                print "The enemy spy has escaped with all your secrets..."
                print "Game Over"
                
    #check if player would like to play again
    correct_input = False
    while correct_input != True:
        play_again = raw_input("Would you like to play again? (Y/N)")
        play_again = play_again.upper()
        if play_again == "Y" or play_again == "N":
            correct_input = True
        else:
            print "Please enter 'Y' or 'N'"
        

#give user a chance to read final output
raw_input("Press Enter to exit...")

