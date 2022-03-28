# Compute whether an integer is even.

###################################################
# Is even formula
# Student should enter function on the next lines.
def is_even(number):
    return number % 2 == 0


###################################################
# Tests
# Student should not change this code.

def test(number):
    """Tests the is_even function."""
    if is_even(number):
        print number, "is even."
    else:
        print number, "is odd."

test(8)
test(3)
test(12)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#8 is even.
#3 is odd.
#12 is even.
