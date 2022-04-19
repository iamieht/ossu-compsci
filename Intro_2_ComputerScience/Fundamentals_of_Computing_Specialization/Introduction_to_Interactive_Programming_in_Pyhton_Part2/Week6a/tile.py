# Define an initializer for the Tile class, create a Tile object


#################################################
# Student adds code where appropriate    

# definition of a Tile class
class Tile:
    
    def __init__(self, num):
        self.number = num

    
# create two tiles with numbers 3 and 4   
my_tile = Tile(3)
your_tile = Tile(4)

    
###################################################
# Testing code

print my_tile
print my_tile.number
print your_tile
print your_tile.number

####################################################
# Output of testing code

#<__main__.Tile object>
#3
#<__main__.Tile object>
#4