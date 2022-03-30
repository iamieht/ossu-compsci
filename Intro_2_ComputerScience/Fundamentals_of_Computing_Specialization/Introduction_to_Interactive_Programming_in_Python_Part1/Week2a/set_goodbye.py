# Printing "Goodbye" with a global message variable

###################################################
# Student should enter function on the next lines.
def set_goodbye():
    global message
    message = "Goodbye"
    print message


###################################################
# Tests

message = "Hello"
print message
set_goodbye()
print message

message = "Ciao"
print message
set_goodbye()
print message


###################################################
# Output

#Hello
#Goodbye
#Goodbye
#Ciao
#Goodbye
#Goodbye