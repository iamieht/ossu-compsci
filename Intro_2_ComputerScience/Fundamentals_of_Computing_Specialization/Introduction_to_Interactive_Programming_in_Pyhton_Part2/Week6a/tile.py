# Add a __str__ class to the Tile class

#################################################
# Student adds code where appropriate    

# definition of a Tile class
class Tile:
    
    # definition of intializer
    def __init__(self, val, exp):
        self.number = val
        self.exposed = exp
        
    # definition of getter for number
    def get_number(self):
        return self.number
    
    # check whether tile is exposed
    def is_exposed(self):
        return self.exposed
    
    # expose the tile
    def expose_tile(self):
        self.exposed = True
    
    # hide the tile       
    def hide_tile(self):
        self.exposed = False
        
    # string method for tiles    
    def __str__(self):
        return 'number is ' + str(self.get_number()) + ', ' + 'exposed is ' + str(self.is_exposed())
    
# create a Tile called my_tile with number 3 that is exposed    
my_tile = Tile(3, True)

    
###################################################
# Testing code

print my_tile
my_tile.hide_tile()
print my_tile
my_tile.expose_tile()
print my_tile


####################################################
# Output of testing code

#number is 3, exposed is True
#number is 3, exposed is False
#number is 3, exposed is True
