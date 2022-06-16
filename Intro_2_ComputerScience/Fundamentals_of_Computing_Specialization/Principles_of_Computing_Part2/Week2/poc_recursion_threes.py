"""
Example of a recursive function that computes the
number of threes in the decimal form of a number
"""

def number_of_threes(num):
    """
    Takes a non-negative integer num and compute the 
    number of threes in its decimal form
    Returns an integer
    """
    if num == 0:
        return 0
    else:
        unit_digit = num % 10
        threes_in_rest = number_of_threes(num // 10)
        if unit_digit == 3:
            return threes_in_rest + 1
        else:
            return threes_in_rest
    
def test_number_of_threes():
    """
    Some test cases for number_of_threes
    """
    print "Computed:", number_of_threes(0), "Expected: 0"
    print "Computed:", number_of_threes(5), "Expected: 0"
    print "Computed:", number_of_threes(3), "Expected: 1"
    print "Computed:", number_of_threes(33), "Expected: 2"
    print "Computed:", number_of_threes(34534), "Expected: 2"
    
test_number_of_threes()