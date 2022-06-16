"""
Example of a recursive function that whether
a list contains a specified element
"""

def is_member(my_list, elem):
    """
    Take list my_list and determines whether elem is in my_list
    Returns True or False
    """
    if my_list == []:
        return False
    else:
        first_elem  = my_list[0]
        if first_elem == elem:
            return True
        else:
            return is_member(my_list[1 :], elem)
    
def test_is_member():
    """
    Some test cases for is_member
    """
    print "Computed:", is_member([], 1), "Expected: False"
    print "Computed:", is_member([1], 1), "Expected: True"
    print "Computed:", is_member(['c', 'a', 't'], 't'), "Expected: True"
    print "Computed:", is_member(['c', 'a', 't'], 'd'), "Expected: False"
    
test_is_member()