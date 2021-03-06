"""
Template testing suite for Solitaire Mancala
"""

import poc_simpletest

def run_suite(game_class):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()    
    
    # create a game
    game = game_class()
    
    # add tests using suite.run_test(....) here

    # test the initial configuration of the board using the str method
    suite.run_test(str(game), str([0]), "Test #0: init")

    # check the str, get_num_seeds and is_legal_move methods
    config1 = [0, 0, 1, 1, 3, 5, 0]    
    game.set_board(config1)   
    suite.run_test(str(game), str([0, 5, 3, 1, 1, 0, 0]), "Test #1a: str")
    suite.run_test(game.get_num_seeds(1), config1[1], "Test #1b: get_num_seeds")
    suite.run_test(game.get_num_seeds(3), config1[3], "Test #1c: get_num_seeds")
    suite.run_test(game.get_num_seeds(5), config1[5], "Test #1d: get_num_seeds")
    suite.run_test(game.is_legal_move(0), False, "Test #2a: is_legal_move")
    suite.run_test(game.is_legal_move(5), True, "Test #2b: is_legal_move")
    suite.run_test(game.is_legal_move(4), False, "Test #2c: is_legal_move")
    
    # check apply move
    game.apply_move(5)
    suite.run_test(str(game), str([0,0,4,2,2,1,1]), "Test #3: apply_move")
    suite.run_test(game.choose_move(), game.choose_move(), "Test #4: choose_move")
    
    # Check is_game_won
    suite.run_test(game.is_game_won(), False, "Test #5: is_game_won")
    
    # Check plan moves
    config2 = [0, 0, 1, 1, 3, 5, 0]
    game2 = game_class()
    game2.set_board(config2)
    suite.run_test(str(game2.plan_moves()), str([5, 1, 2, 1, 4, 1, 3, 1, 2, 1]), "Test #6: plan_moves")
    
    # report number of tests and failures
    suite.report_results()
