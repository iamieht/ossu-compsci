"""
Example of a recursive function that inserts the character
'x' between all adjacent pairs of characters in a string
"""

def insert_x(my_string):
    """
    Takes a string my_string and add the character 'x'
    between all pairs of adjacent characters in my_string
    Returns a string
    """
    if len(my_string) <= 1:
        return my_string
    else:
        first_character = my_string[0]
        rest_inserted = insert_x(my_string[1 :])
        return first_character + 'x' + rest_inserted
    
def test_insert_x():
    """
    Some test cases for insert_x
    """
    print "Computed:", "\"" + insert_x("") + "\"", "Expected: \"\""
    print "Computed:", "\"" + insert_x("c") + "\"", "Expected: \"c\""
    print "Computed:", "\"" + insert_x("pig") + "\"", "Expected: \"pxixg\""
    print "Computed:", "\"" + insert_x("catdog") + "\"", "Expected: \"cxaxtxdxoxg\""
    
test_insert_x()