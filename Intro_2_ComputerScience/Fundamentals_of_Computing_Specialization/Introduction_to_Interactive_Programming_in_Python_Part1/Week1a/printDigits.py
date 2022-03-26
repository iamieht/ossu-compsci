# Compute and print tens and ones digit of an integer in [0,100).

###################################################
# Digits function
# Student should enter function on the next lines.
def print_digits(digits):
    print "The tens digit is " + str(digits//10) + "," + " and the ones digit is " + str(digits%10) + "."

	
###################################################
# Tests
# Student should not change this code.
	
print_digits(42)
print_digits(99)
print_digits(5)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.
