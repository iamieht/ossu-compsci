# implementation of card game - Memory

import simplegui
import random

card_deck = list(range(0,8)) + list(range(0,8))

# helper function to initialize globals
def new_game():
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for idx in range(len(card_deck)):
        canvas.draw_text(str(card_deck[idx]), (idx*50+25, 60), 36, "White")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# CodeSkulptor: https://py2.codeskulptor.org/#user49_Gzo0xsOhp7_0.py