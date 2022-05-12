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

def pair_elements(aList):
    """
    Group similar elements in pairs
    """
    pass
        
        
#    for idx in range(len(aList)):
#        if aList[idx] == aList[idx+1]:
#            result.append(aList[idx:idx+1])
#            
        
        

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    merged_list = zeros_end(line)
#    merged_list = sublist(merged_list, 2)
    result = []
    zeros = len(line)
    
    for idx in range(len(merged_list)-1):
        if merged_list[idx] == merged_list[idx+1]:
            merged_list[idx] *= 2
            merged_list[idx+1] = 0
            
    result = zeros_end(merged_list)
    
    
    
#    for element in merged_list:
#        if len(element) > 1:
#            if element[0] == element[1]:
#                result.append(element[0] + element[1])
#            else:
#                result.extend(element)
#        else:
#            result.extend(element)
                
#    result.extend((zeros-len(result))*[0])
    return result
    
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
print "=========================="
print "Test Cases merge"
print merge([2, 0, 2, 4])
print merge([0, 0, 2, 2])
print merge([2, 2, 0, 0])
print merge([2, 2, 2, 2, 2])
print merge([8, 16, 16, 8])

#CodeSkulptor: https://py2.codeskulptor.org/#user49_zcnxRetw1j_2.py