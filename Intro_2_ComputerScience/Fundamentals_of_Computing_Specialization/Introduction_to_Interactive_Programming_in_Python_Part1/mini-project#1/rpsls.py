# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random
# helper functions

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
    
    # print out the message for the player's choice
    print "Player chooses", player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print 'Computer chooses', comp_choice
    
    # compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if diff == 1 or diff == 2:
        print 'Computer wins!'
    elif diff == 3 or diff == 4:
        print 'Player wins!'
    else:
        print 'Player and computer tie!'
    
    # print a blank line to separate consecutive games
    print
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
# Test Cases name_to_number
#print 'Test Cases name_to_number'
#print name_to_number('rock')
#print name_to_number('Spock')
#print name_to_number('paper')
#print name_to_number('lizard')
#print name_to_number('scissors')
#print name_to_number('t-rex')
#print 
#print 'Test Cases number_to_name'
#print number_to_name(0)
#print number_to_name(1)
#print number_to_name(2)
#print number_to_name(3)
#print number_to_name(4)
#print number_to_name(5)


