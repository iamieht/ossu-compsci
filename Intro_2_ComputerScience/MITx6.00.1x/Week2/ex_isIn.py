def isIn(char, aStr):
    '''
    char: string single character
    aStr: a string in alphabetical order
    '''
    
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        return aStr == char
    else:
        middleChar = len(aStr) // 2
        if aStr[middleChar] == char:
            return True
            #print('middlechar' ,aStr[middleChar])
        elif aStr[middleChar] < char:
            #print('aStr', aStr[middleChar+1:] )
            return isIn(char, aStr[middleChar+1:])
            
        else:
            #print('aStr', aStr[:middleChar] )
            return isIn(char, aStr[:middleChar])
            

# Test Cases
print(isIn('a', '')) #False
print(isIn('g', 'ahkkkwwxz')) #False
print(isIn('u', 'aceefhikklqsuuv')) #True
print(isIn('q', 'cqry')) #True
print(isIn('l', 'aacjklnrtxz')) #True
print(isIn('x', 'dglnqrsvwxyz')) #True
print(isIn('j', 'cdegiuyz')) #False
print(isIn('p', 'degjmmmsuuvwxxy')) #False
print(isIn('p', 'aaacfhijkkkmorsuzz')) #False
print(isIn('h', 'bccdefffhijnnopvxxzz')) #True