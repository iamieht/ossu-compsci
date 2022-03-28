# Compute whether a person is cool.

###################################################
# Is cool formula
# Student should enter function on the next lines.
def is_cool(name):
    if name == 'John' or name == 'Joe' or name == 'Stephen':
        return True
    else:
        return False


###################################################
# Tests
# Student should not change this code.

def test(name):
    """Tests the is_cool function."""
    
    if is_cool(name):
        print name, "is cool."
    else:
        print name, "is not cool."

test("Joe")
test("John")
test("Stephen")
test("Scott")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe is cool.
#John is cool.
#Stephen is cool.
#Scott is not cool.
