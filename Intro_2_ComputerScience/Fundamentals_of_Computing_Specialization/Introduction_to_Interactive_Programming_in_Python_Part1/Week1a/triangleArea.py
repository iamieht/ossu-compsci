# Compute the area of a triangle (using Heron's formula),
# given its side lengths.

###################################################
# Triangle area (Heron's) formula
# Student should enter function on the next lines.
# Hint:  Also define point_distance as use it as a helper function.
def triangle_area(x0,y0,x1,y1,x2,y2):
    a = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
    b = ((x0 - x2) ** 2 + (y0 - y2) ** 2) ** 0.5
    c = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


###################################################
# Tests
# Student should not change this code.

def test(x0, y0, x1, y1, x2, y2):
	print "A triangle with vertices (" + str(x0) + "," + str(y0) + "),",
	print "(" + str(x1) + "," + str(y1) + "), and",
	print "(" + str(x2) + "," + str(y2) + ") has an area of",
	print str(triangle_area(x0, y0, x1, y1, x2, y2)) + "."

test(0, 0, 3, 4, 1, 1)
test(-2, 4, 1, 6, 2, 1)
test(10, 0, 0, 0, 0, 10)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.
