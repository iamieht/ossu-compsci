"""
Template testing suite for 2048
"""

import poc_simpletest

def run_suite(game_class):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()    
    
    # create a game
    #game = game_class(h,g)
    
    # add tests using suite.run_test(....) here

    # test the initial configuration of the board using the str method
    suite.run_test(str(game_class), str(game_class), "Test #0: init")
    suite.run_test(str(game_class.reset()), str(game_class.reset()), "Test #1: reset()")
    suite.run_test(str(game_class.new_tile()), str(game_class.new_tile()), "Test #2: new_tile()")
    
    # report number of tests and failures
    suite.report_results()


#CodeSkulptor: https://py2.codeskulptor.org/#user49_hUyrMJxgZ0_19.py