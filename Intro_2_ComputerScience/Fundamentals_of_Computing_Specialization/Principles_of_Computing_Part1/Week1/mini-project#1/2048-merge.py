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
    zeros = []
    for element in aList:
        if element == 0:
            zeros.append(element)
        else:
            newList.append(element)
            
    return newList + zeros
        

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    return []



# Test Cases
test_list = [2, 0, 2, 2]
print zeros_end(test_list)
print zeros_end([2, 0, 2, 4])
print zeros_end([0, 0, 2, 2])
print zeros_end([2, 2, 0, 0])
print zeros_end([2, 2, 2, 2, 2])
print zeros_end([8, 16, 16, 8])