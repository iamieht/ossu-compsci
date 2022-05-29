class TTTBoard:
    """
    Class to represent a Tic-Tac-Toe board.
    """

    def __init__(self, dim, reverse = False, board = None):
        """
        Initialize the TTTBoard object with the given dimension and 
        whether or not the game should be reversed.
        """
            
    def __str__(self):
        """
        Human readable representation of the board.
        """

    def get_dim(self):
        """
        Return the dimension of the board.
        """
    
    def square(self, row, col):
        """
        Returns one of the three constants EMPTY, PLAYERX, or PLAYERO 
        that correspond to the contents of the board at position (row, col).
        """

    def get_empty_squares(self):
        """
        Return a list of (row, col) tuples for all empty squares
        """

    def move(self, row, col, player):
        """
        Place player on the board at position (row, col).
        player should be either the constant PLAYERX or PLAYERO.
        Does nothing if board square is not empty.
        """

    def check_win(self):
        """
        Returns a constant associated with the state of the game
            If PLAYERX wins, returns PLAYERX.
            If PLAYERO wins, returns PLAYERO.
            If game is drawn, returns DRAW.
            If game is in progress, returns None.
        """
            
    def clone(self):
        """
        Return a copy of the board.
        """