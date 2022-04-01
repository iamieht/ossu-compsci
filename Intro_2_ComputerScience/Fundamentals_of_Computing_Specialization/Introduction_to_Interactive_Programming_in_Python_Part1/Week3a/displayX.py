# Display an X

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Draw handler
def draw(canvas):
    canvas.draw_text("X", [0,32], 48, "White")

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Draw X", 96, 96)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
