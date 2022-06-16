"""
Example of a recursive function that computes a triangular sum
"""

def triangular_sum(num):
    """
    Take an integer num
    Returns 0 + 1 + ... + (num - 1) + num
    """
    if num == 0:
        return 0
    else:
        return num + triangular_sum(num - 1)
    
def test_triangular_sum():
    """
    Some test cases for triangular_sum
    """
    print "Computed:", triangular_sum(0), "Expected: 0"
    print "Computed:", triangular_sum(1), "Expected: 1"
    print "Computed:", triangular_sum(3), "Expected: 6"
    print "Computed:", triangular_sum(10), "Expected: 55"
    
test_triangular_sum()