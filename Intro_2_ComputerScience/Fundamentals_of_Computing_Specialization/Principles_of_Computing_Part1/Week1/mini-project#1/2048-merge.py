"""
Merge function for 2048 game.
"""
def zeros_end(aList):
    """
    Function that moves non-zero elements of a list to
    the beginning and zeros at the end.
    Returns a new list.
    """
    newList = []
    zeros = 0
    for element in aList:
        if element == 0:
            zeros += 1
        else:
            newList.append(element)
            
    newList.extend(zeros*[0])
    return newList

def sublist(aList, num):
    """
    Function that creates a sublist group by number of elements
    num: Int
    """
    aList2 = list()
    for i in range(0, len(aList), num):
        aList2.append(aList[i:i+num])
    
    return aList2
        

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    pass
    
#    for idx in range(0,len(new_line)-1,2):
#        if new_line[idx] == new_line[idx+1]:
#            new_line2.append(new_line[idx]+new_line[idx+1])
#        else:
#            new_line2.append(new_line[idx])
#            
#    return new_line2




print "Test Cases zeros_end"
print zeros_end([2, 0, 2, 4])
print zeros_end([0, 0, 2, 2])
print zeros_end([2, 2, 0, 0])
print zeros_end([2, 2, 2, 2, 2])
print zeros_end([8, 16, 16, 8])
print "=========================="
print "Test sublist"
print sublist([2, 0, 2, 4], 2)
print sublist([0, 0, 2, 2], 2)
print sublist([2, 2, 0, 0], 2)
print sublist([2, 2, 2, 2, 2], 2)
print sublist([8, 16, 16, 8], 2)
#print ""
#print "Test Cases merge"
#print merge([2, 0, 2, 2])
#print merge([2, 0, 2, 4])
#print merge([0, 0, 2, 2])
#print merge([2, 2, 0, 0])
#print merge([2, 2, 2, 2, 2])
#print merge([8, 16, 16, 8])

#CodeSkulptor: https://py2.codeskulptor.org/#user49_zcnxRetw1j_1.py