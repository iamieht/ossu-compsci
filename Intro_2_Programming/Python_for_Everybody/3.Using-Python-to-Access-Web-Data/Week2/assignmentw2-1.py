'''
Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
'''
import re
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_1179041.txt"
handle = open(name)

numbers = re.findall('[0-9]+', handle.read())
numbers = list(map(int, numbers))
print(sum(numbers))
