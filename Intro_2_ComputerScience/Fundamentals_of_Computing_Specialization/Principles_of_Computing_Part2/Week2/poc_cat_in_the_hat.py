"""
Recursion according to the "Cat in the Hat"
"""


def get_next_cat(current_cat):
    """
    Helper function to get next cat
    """
    if current_cat == "Cat in the Hat":
        return "Little Cat A"
    elif current_cat != "Little Cat Z":
        return "Little Cat " + chr(ord(current_cat[-1]) + 1)
    else:
        return "Voom"


def clean_up(helper_cat):
    """
    Recursive function that prints out story
    """
    if helper_cat == "Voom":
        print helper_cat + ": I got this. Mess is all cleaned up!"
    else:
        next_cat = get_next_cat(helper_cat)
        print helper_cat + ": I'll have", next_cat, "clean up!"
        clean_up(next_cat)
        
# get those cats to work!!!!!
clean_up("Cat in the Hat")
        