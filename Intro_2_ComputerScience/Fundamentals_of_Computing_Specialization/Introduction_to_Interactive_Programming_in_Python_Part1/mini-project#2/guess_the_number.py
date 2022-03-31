# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

#Global Variables
num_range = 100
remaining_guesses = 7
total_guess = 7
# helper function to start and restart the game
def new_game():
    '''
    Generates a new game
    '''
    global secret_number, remaining_guesses, total_guess
    remaining_guesses = total_guess
    secret_number = random.randrange(0, num_range)
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is", total_guess
    print


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range, total_guess
    num_range = 100
    total_guess = 7
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range, total_guess
    num_range = 1000
    total_guess = 10
    new_game()
    
    
def input_guess(guess):
    '''
    Main game logic
    guess: string
    check if guess == secret_number
    '''
    global remaining_guesses
    guess = int(guess)
    remaining_guesses -= 1
    
    print "Guess was", int(guess)
    if remaining_guesses > 0:        
        if guess == secret_number:
            print "Number of remaining guesses is", remaining_guesses
            print "Correct"
            print
            new_game()
        elif guess > secret_number:
            print "Number of remaining guesses is", remaining_guesses
            print "Lower!"
            print
        elif guess < secret_number:
            print "Number of remaining guesses is", remaining_guesses
            print "Higher!"
            print
    elif remaining_guesses == 0:
        if guess == secret_number:
            print "Number of remaining guesses is", remaining_guesses
            print "Correct!!!"
            print
            new_game()
        else:
            print "Number of remaining guesses is", remaining_guesses
            print "You ran out of guesses. The number was", secret_number
            print
            new_game()

    
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
# CodeSkulptor link: https://py2.codeskulptor.org/#user49_UeT91q4XT4_0.py