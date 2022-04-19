# Define a getter method for the Tile class

#################################################
# Student adds code where appropriate    

# definition of a Tile class
class Tile:
    
    # definition of intializer
    def __init__(self, num):
        self.number = num
        
    # definition of getter for number
    def get_number(self):
        return self.number
    
# create a Tile called my_tile with number 3    
my_tile = Tile(3)

# get the number of my_tile and assign to tile_number
# Note "tile_number = my_tile.number" works, but is incorrect
tile_number = my_tile.get_number()
    
    
###################################################
# Testing code

print my_tile
print tile_number


####################################################
# Output of testing code

#<__main__.Tile object>
#3