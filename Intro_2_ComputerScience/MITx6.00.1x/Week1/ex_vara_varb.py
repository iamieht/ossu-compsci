'''
Assume that two variables, varA and varB, are assigned values, either numbers or strings.

Write a piece of Python code that evaluates varA and varB, and then prints out one of the following messages:
"string involved" if either varA or varB are strings
"bigger" if varA is larger than varB
"equal" if varA is equal to varB
"smaller" if varA is smaller than varB
'''
# Test cases
### Case 1 'string involved'
#varA = 'str1'
#varB = 'str2'
### Case 2 'string involved'
# varA = 'str1'
# varB = 2
# Case 3 'bigger'
#varA = 20
#varB = 10
# Case 4 'smaller'
varA = 1
varB = 20

# Main prog
if type(varA) == str or type(varB) == str:
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
else:
    print('smaller')
