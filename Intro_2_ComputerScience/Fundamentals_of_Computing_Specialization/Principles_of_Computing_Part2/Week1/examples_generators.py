"""
Generator examples.
"""

# A list comprehension
print "max in list:", max([num * 2 - 3 for num in range(7)])

# A generator expression
print "max in gen:", max(num * 2 - 3 for num in range(7))

# A generator function
def genfunc(limit):
    num = 0
    while num < limit:
        yield num
        num = num + 1

print genfunc(7)
        
# Iteration using a generator function
print "Iterate over generator:"
for number in genfunc(7):
    print number
    
# Pass to functions expecting a sequence
print "max in gen func:", max(genfunc(4))

# Use return to end generator
def genfunc2(endfunc):
    num = 0
    while True:
        if endfunc(num):
            return
        yield num
        num = num + 1
        
def endfn(num):
    if num == 7:
        return True
    return False

print "Iterate over second generator:"
for number in genfunc2(endfn):
    print number