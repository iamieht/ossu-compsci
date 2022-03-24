# Compute the distance between the points (x0, y0) and (x1, y1).

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
x0 = 2
y0 = 2
x1 = 5
y1 = 6


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
#x0 = 1
#y0 = 1
#x1 = 2
#y1 = 2


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
#x0 = 0
#y0 = 0
#x1 = 3
#y1 = 4


###################################################
# Distance formula
# Student should enter formula on the next line.
distance = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
# Hint: You need to use the power operation ** .


###################################################
# Test output
# Student should not change this code.

print "The distance from (" + str(x0) + ", " + str(y0) + ") to", 
print "(" + str(x1) + ", " + str(y1) + ") is " + str(distance) + "."


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#The distance from (2, 2) to (5, 6) is 5.0.

# Test 2 output:
#The distance from (1, 1) to (2, 2) is 1.41421356237.

# Test 3 output:
#The distance from (0, 0) to (3, 4) is 5.0.
