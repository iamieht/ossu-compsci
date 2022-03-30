# Open a frame

###################################################
# Open frame
# Student should add code where relevant to the following.
import simplegui

message = "My first frame!"

# Handler for mouse click
def click():
    print message

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("My first frame", 100, 200)
frame.add_button("Click me", click)

# Start
frame.start()


