"""
Clone of 2048 game.
"""

import poc_2048_gui
import random


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
        """
        constructor
        """
        self._height = grid_height
        self._width = grid_width
        self._board = []
        self._indices = {UP: [(0,col)for col in range(self._width)] ,
                   DOWN: [(self._height-1,col)for col in range(self._width)],
                   LEFT: [(row,0)for row in range(self._height)],
                   RIGHT: [(row,self._width-1)for row in range(self._height)]}
        self.reset()
        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._board = [[0 for col in range(self._width)] for row in range(self._height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        str_board = ""
        for index in range(len(self._board)):
            str_board += str(self._board[index]) + "\n"
        
        return str_board

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width
    
    def cut(self , start , direction , steps):
        """
        makes a list and return it
        """
        the_list = []
        for step in range(steps):
            row = start[0] + step * direction[0]
            col = start[1] + step * direction[1]
            the_list.append(self._board[row][col])
        return the_list
    
    def modify(self , start , direction , steps , merged):
        """
        modifies the grid
        """
        for step in range(steps):
            row = start[0] + step * direction[0]
            col = start[1] + step * direction[1]
            self._board[row][col] = merged[step]

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        steps = self._height
        changed = False
        if direction == RIGHT or direction == LEFT:
            steps = self._width
        for index in self._indices[direction]:
            cutted = self.cut(index,OFFSETS[direction], steps)
            merged = merge(cutted)
            if cutted != merged :
                changed = True
            self.modify(index,OFFSETS[direction], steps , merged)
        if changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        number = random.random()          
        col = 0
        row = 0
        not_found = True
        
        while not_found:
            col = random.randrange(self._width)
            row = random.randrange(self._height)
            if self._board[row][col] == 0:
                not_found = False
        
        if number >= 0.9:
            self._board[row][col] = 4
        else:
            self._board[row][col] = 2

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._board[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

#Test Suite
#import user49_rrK9yzg2Bo_9 as poc_2048_testsuite
#poc_2048_testsuite.run_suite(TwentyFortyEight(4,4))



#CodeSkulptor: https://py2.codeskulptor.org/#user49_hxMrpktg4aIs5Sk.py