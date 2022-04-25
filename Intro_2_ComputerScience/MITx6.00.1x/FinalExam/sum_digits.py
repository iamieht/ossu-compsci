def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
        If there are no digits in s it raises a ValueError exception. """

    result = 0
    isNumber = False
    for char in s:
        if char in '0123456789':
            isNumber = True
            result += int(char)

    if not isNumber:
        raise ValueError('There are no numbers in', s)
    else:
        return result    


# Test Case
print(sum_digits("a;35d4"))
print(sum_digits("a;d"))
    