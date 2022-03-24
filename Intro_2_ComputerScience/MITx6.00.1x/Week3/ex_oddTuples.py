def oddTuples(aTuple):
    '''
    aTuple: Tuple
    returns every other element of aTuple as Tuple
    '''
    resultTuple = ()

    for idx in range(0, len(aTuple), 2):
        resultTuple += (aTuple[idx],)

    return resultTuple

# Test Case
print(oddTuples(('I', 'am', 'a', 'test', 'tuple'))) #('I', 'a', 'tuple')
print(oddTuples(())) #()
print(oddTuples((13,))) #(13,)
print(oddTuples((3, 0, 9, 17, 16))) #(3, 9, 16)
print(oddTuples((0, 20, 8, 9, 19, 18, 9, 18))) #(0, 8, 19, 9)
print(oddTuples((5, 3, 11, 1, 6, 1, 10, 6))) #(5, 11, 6, 10)
print(oddTuples((12, 7, 7, 9))) #(12, 7)
print(oddTuples((10, 1, 11, 12, 10, 3, 5, 17, 2))) #(10, 11, 10, 5, 2)
print(oddTuples((20, 9, 10, 17, 12, 9, 10))) #(20, 10, 12, 10)
print(oddTuples((3, 4, 7, 4, 3, 18))) #(3, 7, 3)
print(oddTuples((13, 17, 1, 7, 6))) #(13, 1, 6)