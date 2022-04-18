# implementation of card game - Memory

import simplegui
import random

card_deck = list(range(0,8)) + list(range(0,8))
card_deck_exposed = 16*[False]


# helper function to initialize globals
def new_game():
    global card_deck
    random.shuffle(card_deck)

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for idx in range(1,len(card_deck) + 1):
        if card_deck_exposed[idx-1]:
            canvas.draw_text(str(card_deck[idx-1]), (idx*50-35, 65), 48, "White")
        else:
            a = (idx * 50) - 50
            b = 0
            c = idx * 50
            d = 100
            canvas.draw_polygon([(a, b), (a, d), (c, d), (c, b)], 2, "Black", "Green")


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