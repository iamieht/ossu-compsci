"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    # base case : if game is over, return the score and (-1, -1) as move
    if board.check_win() is not None:
        return (SCORES[board.check_win()], (-1, -1))

    # worst possible result for recursion. player loses.
    game_result = (-1, (-1, -1))

    for move in board.get_empty_squares():
        # clone the board so that recurrent calls for mm_move will not modify the original board.
        copiedboard = board.clone()
        # apply a move with the current player
        copiedboard.move(move[0], move[1], player)

        score, _ = mm_move(copiedboard, provided.switch_player(player))

        # best possible choice found already
        if score * SCORES[player] == 1:
            return score, move
        elif score * SCORES[player] > game_result[0]:
            game_result = (score, move)
        elif game_result[0] == -1:
            game_result = (game_result[0], move)

    return game_result[0] * SCORES[player], game_result[1]

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

#CodeSkulptor: https://py2.codeskulptor.org/#user49_NSJ66ngZXm_1.py
