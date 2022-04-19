# Add an exposed field to a Tile object with three methods

#################################################
# Student adds code where appropriate    

# definition of a Tile class
class Tile:
    
    # definition of intializer
    def __init__(self, num, exp):
        self.number = num
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
    
    
# create a Tile called my_tile with number 3 that is exposed    
my_tile = Tile(3, True)

    
###################################################
# Testing code

print my_tile
print my_tile.is_exposed()
my_tile.hide_tile()
print my_tile.is_exposed()
my_tile.expose_tile()
print my_tile.is_exposed()


####################################################
# Output of testing code

#<__main__.Tile object>
#True
#False
#True
