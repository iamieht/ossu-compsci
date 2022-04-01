# Define a function that returns formatted minutes and seconds

###################################################
# Time formatting function
# Student should enter function on the next lines.
def format_time(seconds):
    '''
    seconds: int range(0, 3600)
    returns time in min and seconds as string
    '''
    return str(seconds // 60) + " minutes and " + str(seconds % 60) + " seconds"
    


###################################################
# Tests

print format_time(23)
print format_time(1237)
print format_time(0)
print format_time(1860)

###################################################
# Output to console
#0 minutes and 23 seconds
#20 minutes and 37 seconds
#0 minutes and 0 seconds
#31 minutes and 0 seconds
