# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Functions that compute RPSLS
def name_to_number(name):
    """
    name: String
    returns an int that uniquely represents the string
    """
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return 'Error: invalid input'

def number_to_name(number):
    """
    number: non-negative int
    returns a String that uniquely represents the number
    """
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'Error: invalid input'

def rpsls(player_choice):
    print "Player chooses", player_choice
    player_number = name_to_number(player_choice)
    
    if type(player_number) != int:
        print "Error: invalid input", player_choice
        print
        exit
    else:    
        comp_number = random.randrange(0,5)
        comp_choice = number_to_name(comp_number)
        print 'Computer chooses', comp_choice
        diff = (comp_number - player_number) % 5

        if diff == 1 or diff == 2:
            print 'Computer wins!'
        elif diff == 3 or diff == 4:
            print 'Player wins!'
        else:
            print 'Player and computer tie!'

        print
    
# Handler for input field
def get_guess(guess):
    rpsls(guess)
    


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
