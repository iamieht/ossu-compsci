# Compute the future value of a given present value, annual rate, and number of years.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
present_value = 1000
annual_rate = 7
years = 10


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
#present_value = 200
#annual_rate = 4
#years = 5


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
#present_value = 1000
#annual_rate = 3
#years = 20


###################################################
# Future value formula
# Student should enter formula on the next line.
future_value = present_value * (1 + 0.01 * annual_rate) ** years


###################################################
# Test output
# Student should not change this code.

print "The future value of $" + str(present_value) + " in " + str(years),
print "years at an annual rate of " + str(annual_rate) + "% is $" + str(future_value) + "."


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#The future value of $1000 in 10 years at an annual rate of 7% is $1967.15135729.

# Test 2 output:
#The future value of $200 in 5 years at an annual rate of 4% is $243.33058048.

# Test 3 output:
#The future value of $1000 in 20 years at an annual rate of 3% is $1806.11123467.
