def applyToEach(L,f):
    '''
    L is a list
    f is a function
    mutates L by replacing each element, e, of L by f(e)
    '''
    for i in range(len(L)):
        L[i] = f(L[i])