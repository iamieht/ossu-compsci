# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

#Global Variables
num_range = 100


# helper function to start and restart the game
def new_game():
    '''
    Generates a new game
    '''
    global secret_number, remaining_guesses
    secret_number = random.randrange(0, num_range)
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is"
    print


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
    
def input_guess(guess):
    '''
    Main game logis
    guess: string
    check if guess == secret_number
    '''
    guess = int(guess)
    print "Guess was", int(guess)
    
    if guess == secret_number:
        print "Correct"
        
    elif guess > secret_number:
        print "Lower!"
        print
    else:
        print "Higher!"
        print

    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 150)
frame.add_button("Range is [0, 1000)", range1000, 150)
frame.add_input("Enter a number:", input_guess, 150)
frame.start()


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
