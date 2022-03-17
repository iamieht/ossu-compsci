'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
'''
# Test Cases
#s = 'abcbcd' #Longest substring in alphabetical order is: abc
#s = 'azcbobobegghakl' #Longest substring in alphabetical order is: beggh
#s = 'vecmxxlytamcwzvicguop' #Longest substring in alphabetical order is: cmxx
#s = 'yeycakrnkffztrb' #Longest substring in alphabetical order is: akr
#s = 'gfpjvjnbeygaeopxghb' #Longest substring in alphabetical order is: aeopx
s = 'abcdefghijklmnopqrstuvwxyz' #Longest substring in alphabetical order is: abcdefghijklmnopqrstuvwxyz
# Main Prog
currentLongest = s[0]
longest = ''

for idx in range(1,len(s)):
    if s[idx] >= s[idx-1]:
        currentLongest += s[idx]
        if len(currentLongest) > len(longest):
            longest = currentLongest
    else:
        if len(currentLongest) > len(longest):
            longest = currentLongest
            currentLongest = s[idx]
        else:
            currentLongest = s[idx]



print('Longest substring in alphabetical order is:', longest)