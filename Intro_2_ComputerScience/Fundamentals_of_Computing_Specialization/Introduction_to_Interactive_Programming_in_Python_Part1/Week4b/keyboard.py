# Key board debugging - debug and fix the code below

import simplegui

message = "Welcome!"

# Handler for keydown
def keydown(key):
    global message
    if key == simplegui.KEY_MAP["up"]:
        message = "Up arrow"
    elif key == simplegui.KEY_MAP["down"]:
        message = "Down arrow"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
