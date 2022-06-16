"""
Example of a recursive function that computes the
greatest common divisor of two numbers using Euclid's algorithm.
"""

def gcd(num1, num2):
    """
    Takes non-negative integers num1 and num2 and
    returns the greatest common divisor of these numbers
    """
    if num2 > num1:
        return gcd(num2, num1)
    else:
        if num2 == 0:
            return num1
        else:
            return gcd(num1 - num2, num2)
    
    
def test_gcd():
    """
    Some test cases for gcd
    """
    print "Computed:", gcd(0, 0), "Expected: 0"
    print "Computed:", gcd(3, 0), "Expected: 3"
    print "Computed:", gcd(0, 2), "Expected: 2"
    print "Computed:", gcd(12, 4), "Expected: 4"
    print "Computed:", gcd(24, 18), "Expected: 6"
    
test_gcd()