"""
Merge function for 2048 game.
"""
def zeros_end(alist):
    """
    Function that moves non-zero elements of a list to
    the beginning and zeros at the end.
    Returns a new list.
    """
    new_list = []
    zeros = 0
    for element in alist:
        if element == 0:
            zeros += 1
        else:
            new_list.append(element)
            
    new_list.extend(zeros*[0])
    return new_list

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = zeros_end(line)
    result = []
    
    for idx in range(len(new_line)-1):
        if new_line[idx] == new_line[idx+1]:
            new_line[idx] *= 2
            new_line[idx+1] = 0
            
    result = zeros_end(new_line)
    return result


print "Test Cases zeros_end"
print zeros_end([2, 0, 2, 4])
print zeros_end([0, 0, 2, 2])
print zeros_end([2, 2, 0, 0])
print zeros_end([2, 2, 2, 2, 2])
print zeros_end([8, 16, 16, 8])
print "=========================="

print "Test Cases merge"
print merge([2, 0, 2, 4])
print merge([0, 0, 2, 2])
print merge([2, 2, 0, 0])
print merge([2, 2, 2, 2, 2])
print merge([8, 16, 16, 8])

#CodeSkulptor: https://py2.codeskulptor.org/#user49_zcnxRetw1j_4.py