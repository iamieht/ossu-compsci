"""
Number of possible Tic-Tac-Toe boards where X goes first.
Note that note all boards count are legal 
since they may have a win for both X and O.
"""

import math

NUM_SQUARES = 9

def count_boards(num_X, num_O):
    """
    Compute the number of positions with num_X X's
    and num_O O's
    """
    num_E = NUM_SQUARES - num_X - num_O
    X_fact = math.factorial(num_X)
    O_fact = math.factorial(num_O)
    E_fact = math.factorial(num_E)
    
    return math.factorial(NUM_SQUARES) /  \
           (X_fact * O_fact * E_fact)     
    

def total_boards():
    """
    Compute an estimate of the number of valid
    Tic-Tac-Toe boards
    """
    
    total = 0
    for num in range(0, int(NUM_SQUARES / 2)):
        total += count_boards(num, num)
        total += count_boards(num + 1, num)
    
    return total


print total_boards()