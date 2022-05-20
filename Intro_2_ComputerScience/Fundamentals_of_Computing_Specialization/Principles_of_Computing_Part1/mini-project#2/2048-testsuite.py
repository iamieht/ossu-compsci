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
    
    # report number of tests and failures
    suite.report_results()

