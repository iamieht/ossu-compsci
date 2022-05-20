"""
Clone of 2048 game.
"""

import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def zeros_end(alist):
    """
    Function that moves non-zero elements of a list to
    the beginning and zeros at the end.
    Returns a new list.
    """
    new_list = []
    zeros = 0
    for element in alist:
        if element == 0:
            zeros += 1
        else:
            new_list.append(element)
            
    new_list.extend(zeros*[0])
    return new_list

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    new_line = zeros_end(line)
    result = []
    
    for idx in range(len(new_line)-1):
        if new_line[idx] == new_line[idx+1]:
            new_line[idx] *= 2
            new_line[idx+1] = 0
            
    result = zeros_end(new_line)
    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        pass

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        pass

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return ""

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return 0

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return 0

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        pass

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return 0


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
import user49_rrK9yzg2Bo_2 as poc_2048_testsuite
poc_2048_testsuite.run_suite(TwentyFortyEight(4,4))

#CodeSkulptor: https://py2.codeskulptor.org/#user49_hUyrMJxgZ0_3.py