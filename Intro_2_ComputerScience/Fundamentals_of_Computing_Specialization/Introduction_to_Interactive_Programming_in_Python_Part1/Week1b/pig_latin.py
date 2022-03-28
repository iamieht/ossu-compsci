# Compute a (simplified) Pig Latin version of a word.

###################################################
# Pig Latin formula
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    
    # Student should complete function on the next lines.
    if first_letter in 'aeiou':
        return word + "way"
    else:
        return rest_of_word + first_letter + 'ay'


###################################################
# Tests
# Student should not change this code.

def test(word):
    """Tests the pig_latin function."""
    
    print pig_latin(word)
    
test("pig")
test("owl")
test("python")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#igpay
#owlway
#ythonpay
