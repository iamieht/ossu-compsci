def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    vals = {}
    for i in aDict.values():
        vals.setdefault(i,0)
        vals[i] += 1
  
    return sorted(k for k, v in aDict.items() if vals[v] == 1)


#Test Cases
aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
print(uniqueValues(aDict)) # return [1, 3, 8]
aDict2 = {1: 1, 2: 1, 3: 1}
print(uniqueValues(aDict2)) # return []