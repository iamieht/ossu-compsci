def biggest(aDict):
    '''
    aDict: a dictionary where all the values are lists
    returns: the key corresponding to the entry with the largest number of values associated with it.
    '''
    biggestKey = None
    biggest = 0
    for key in aDict.keys():
        if len(aDict[key]) > biggest:
            biggest = len(aDict[key])
            biggestKey = key 

    return biggestKey


# Test Case #1
# animals = {'a':['aardvark'], 'b':['baboon'], 'c':['çoati'], 'd':['donkey', 
# 'dog', 'dingo']}
# 
# print(biggest(animals)) #'d'

# Test Case 2
print(biggest({'a': [], 'b': [1, 7, 5, 4, 3, 18, 10, 0]})) #'b'