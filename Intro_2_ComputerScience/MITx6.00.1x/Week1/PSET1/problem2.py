'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''
# Test Cases
#s = 'azcbobobegghakl' # Number of times bob occurs is: 2
#s = 'kefbooblbboboboboobobobobobobb' #Number of times bob occurs is: 8
s = 'qoboobvoboobbvhv' #Number of times bob occurs is: 0

# Main Prog
bobOccurrence = 0

for idx in range(len(s)):
    if s[idx:idx+3] == 'bob':
        bobOccurrence += 1

print('Number of times bob occurs is:', bobOccurrence)
