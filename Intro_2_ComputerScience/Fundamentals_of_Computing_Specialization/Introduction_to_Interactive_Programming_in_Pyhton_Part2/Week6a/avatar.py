# THE AVATAR CLASS - by Moria Merriweather
# This is similar to quiz 6a problem 7 and problem 8, about BankAccount

# GENERAL DIRECTIONS:
# Make a class Avatar, to be used in a game. 
# An Avatar represents a being or game piece in a game.
# An Avatar needs to have a name, and a hair color.  
# Also, an Avatar carries some amount of gold (in a bag), 
# and can have some gold that is buried.  
# An initial amount of gold to be carried should be specified 
# when creating a new Avatar.  
# A new Avatar starts with 0.0 buried gold.


# DIRECTIONS FOR THE __INIT__ METHOD:
# Here is the beginning of the __init__ method. You need to add
# a few lines to this so that the name, hair_color, and initial_gold
# which are passed in are assigned to fields (variables) in the 
# Avatar class.  The initail_gold will be carried by the Avatar
# in a bag. You also need to add a line so that the Avatar starts 
# with 0.0 in buried gold.

class Avatar:
    def __init__(self, name, hair, initial_gold):
        pass  # replace this line or delete it      
        
        
        
        
# DIRECTIONS FOR OTHER METHODS FOR AVATAR CLASS:
# These methods apply to an existing Avatar:
#
# FIND_GOLD METHOD:
# When an Avatar finds gold, it is added to the gold being carried 
# in a bag.
# The def statement for this method is below.
# Add an indented statement which will add the gold that has been found 
# to the gold that the Avatar is carrying.

    def find_gold(self, amount):
        pass  # replace this line or delete it

# BURY_GOLD METHOD:
# When gold is buried in the ground, the amount of gold is taken out of 
# the gold in the Avatar's bag of gold and this gold is then buried in the 
# ground. It still belongs to the Avatar, and is in their buried gold balance.
# This changes the amount of gold in the Avatar's bag and ALSO the amount
# of gold that the Avatar has buried.
   
    def bury_gold(self, amount):
        pass   # replace this line or delete it
    

# SPRINKLED_WITH_FAIRY_DUST METHOD:
# If the Avatar encounters a fairy and is sprinkled with fairy dust, the gold 
# it is carrying is increased by 10% as a result of a chemical reaction with 
# the fairy dust.  Gold that is in the ground is not affected.
# Add lines to the method below that will increase the balance of the gold
# in the Avatar's bag by 10%.

    def sprinkled_with_fairy_dust(self):
        pass   # replace this line or delete it

# __STR__ METHOD:
# Also create a __str__ method which returns information about the Avatar, 
# including amount of gold in bag, and amount of gold in the ground.
# You can decide on the format to use in printing out these things, just
# be sure to print out at least the name of the Avatar, and the amount
# of gold carried (in bag) and the amount of gold buried (in the ground).
    
    def __str__(self):
        pass   # replace this line or delete it
    

    
    

# TEST SECTION

# The following lines can be used to "test" your implemetation of the Avatar class.
#
# If your methods are implemented correctly, at the end, where it says
# to check the totals for each Avatar:
# ==>  Wild Girl should have 5.75 gold in bag, and 2.5 gold buried.
# ==>  Mad Max should have 28.3195 gold in bag, and 21.5 gold buried.
#
# Remove the # sign in front of the following lines to run the test.
# Highlight it all and hit control-shift-k to uncomment it all at once.

            
#wildgirl = Avatar("Wild Girl", "purple", 5.5)
#print wildgirl
#wildgirl.find_gold(2.0)
#print wildgirl
#wildgirl.sprinkled_with_fairy_dust()
#print wildgirl
#wildgirl.bury_gold(2.5)
#print "=============================="
#print "check totals here:"
#print wildgirl
#print "=============================="
#madmax = Avatar("Mad Max", "black", 6.5)
#print madmax
#madmax.find_gold(25.0)
#print madmax
#madmax.bury_gold(2.0)
#madmax.sprinkled_with_fairy_dust()
#madmax.bury_gold(4.5)
#madmax.sprinkled_with_fairy_dust()
#madmax.find_gold(10.0)
#madmax.bury_gold(15.0)
#madmax.sprinkled_with_fairy_dust()
#print "=============================="
#print "check totals here:"
#print madmax
#print "=============================="

