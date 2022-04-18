# implementation of card game - Memory

import simplegui
import random

card_deck = list(range(0,8)) + list(range(0,8))



# helper function to initialize globals
def new_game():
    global card_deck, state, card_deck_exposed, turns
    card_deck_exposed = 16*[False]
    random.shuffle(card_deck)
    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns))

     
# define event handlers
def mouseclick(pos):
    global state, card1_idx, card2_idx, turns
    idx = pos[0] // 50
    
    if state == 0:
        card_deck_exposed[idx] = True
        card1_idx = idx
        state = 1
    elif state == 1:
        if not card_deck_exposed[idx]:
            card_deck_exposed[idx] = True
            card2_idx = idx
            state = 2
            turns += 1
            label.set_text("Turns = " + str(turns))
    else:
        if not card_deck_exposed[idx]:
            card_deck_exposed[idx] = True
            
            if card_deck[card1_idx] != card_deck[card2_idx]:
                card_deck_exposed[card1_idx] = False
                card_deck_exposed[card2_idx] = False
                
            card1_idx = idx
            state = 1
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global card_deck_exposed
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







# CodeSkulptor: https://py2.codeskulptor.org/#user49_R5ft0B2oe1H1iy9.py