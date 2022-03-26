# Compute the length of a rectangle's perimeter, given its width and height.

###################################################
# Rectangle perimeter formula
# Student should enter function on the next lines.
def rectangle_perimeter(width, height):
    return width * 2 + height * 2


###################################################
# Tests
# Student should not change this code.

def test(width, height):
	print "A rectangle " + str(width) + " inches wide and " + str(height),
	print "inches high has a perimeter of",
	print str(rectangle_perimeter(width, height)) + " inches."

test(4, 7)
test(7, 4)
test(10, 10)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A rectangle 4 inches wide and 7 inches high has a perimeter of 22 inches.
#A rectangle 7 inches wide and 4 inches high has a perimeter of 22 inches.
#A rectangle 10 inches wide and 10 inches high has a perimeter of 40 inches.
