'''
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
'''
# Test Cases
s = 'azcbobobegghakl' #Number of vowels: 5
#s = 'vhgjsjrefxw' #Number of vowels: 1
#s = 'mufjuabozhoahbewylqaud' #Number of vowels: 9

# Main Prog
numberOfVowels = 0

for char in s:
    if char in 'aeiou':
        numberOfVowels += 1

print('Number of vowels:', numberOfVowels)