from ast import alias


def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    bList = []

    for item in aList:
        if not isinstance(item, list):
            bList.append(item)
        else:
            bList += flatten(item)

    return bList

#Test Case
print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])) #[1,'a','cat',2,3,'dog',4,5]