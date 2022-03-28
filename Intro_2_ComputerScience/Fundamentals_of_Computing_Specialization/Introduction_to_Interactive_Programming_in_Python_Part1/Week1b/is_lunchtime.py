# Compute whether the given time is lunchtime.

###################################################
# Is lunchtime formula
# Student should enter function on the next lines.
def is_lunchtime(hour, is_am):
    if hour == 11 and is_am:
        return True
    elif hour == 12 and is_am == False:
        return True
    else:
        return False


###################################################
# Tests
# Student should not change this code.

def test(hour, is_am):
    """Tests the is_lunchtime function."""
    print hour,
    if is_am:
        print "AM",
    else:
        print "PM",
    if is_lunchtime(hour, is_am):
        print "is lunchtime."
    else:
        print "is not lunchtime."

test(11, True)
test(12, True)
test(11, False)
test(12, False)
test(10, False)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#11 AM is lunchtime.
#12 AM is not lunchtime.
#11 PM is not lunchtime.
#12 PM is lunchtime.
#10 PM is not lunchtime.
