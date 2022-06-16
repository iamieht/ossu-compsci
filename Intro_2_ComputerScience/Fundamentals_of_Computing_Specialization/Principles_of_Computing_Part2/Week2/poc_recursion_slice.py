"""
Example of a recursive function that implements list slicing
"""

def slice(my_list, first, last):
    """
    Takes a list my_list and non-negative integer indices
    satisfying 0 <= first <= last <= len(my_list)
    Returns the slice my_list[first : last]
    """
    if my_list == []:
        return []
    else:
        first_elem = my_list.pop(0)
        if first > 0:  
            rest_sliced = slice(my_list, first - 1, last - 1)
            return rest_sliced
        elif last > 0:
            rest_sliced = slice(my_list, 0, last - 1)
            return [first_elem] + rest_sliced
        else:
            return []
    
def test_slice():
    """
    Some test cases for slice
    """
    print "Computed:", slice([], 0, 0), "Expected: []"
    print "Computed:", slice([1], 0, 0), "Expected: []"
    print "Computed:", slice([1], 0, 1), "Expected: [1]"
    print "Computed:", slice([1, 2, 3], 0, 3), "Expected: [1, 2, 3]"
    print "Computed:", slice([1, 2, 3], 1, 2), "Expected: [2]"
    
test_slice()