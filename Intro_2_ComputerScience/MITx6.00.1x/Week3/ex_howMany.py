def how_many(aDict):
    '''
    aDict: a dictionary where all the values are lists
    returns: int, how many values are in the dictionary
    '''
    count = 0
    for key in aDict.keys():
        count += len(aDict[key])
    
    return count

# Test Case #1
# animals = {'a':['aardvark'], 'b':['baboon'], 'c':['çoati'], 'd':['donkey', 'dog', 'dingo']}
# print(how_many(animals))
# Test Case #2
print(how_many({'B': [15], 'u': [10, 15, 5, 2, 6]}))

