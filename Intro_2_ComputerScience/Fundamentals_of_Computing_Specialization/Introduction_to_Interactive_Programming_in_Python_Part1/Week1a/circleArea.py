# Compute the area of a circle, given the length of its radius.

###################################################
# Circle area formula
# Student should enter function on the next lines.
def circle_area(radius):
    return 3.14 * radius ** 2


###################################################
# Tests
# Student should not change this code.

def test(radius):
	print "A circle with a radius of " + str(radius),
	print "inches has an area of",
	print str(circle_area(radius)) + " square inches."

test(8)
test(3)
test(12.9)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A circle with a radius of 8 inches has an area of 201.06192983 square inches.
#A circle with a radius of 3 inches has an area of 28.2743338823 square inches.
#A circle with a radius of 12.9 inches has an area of 522.792433484 square inches.
