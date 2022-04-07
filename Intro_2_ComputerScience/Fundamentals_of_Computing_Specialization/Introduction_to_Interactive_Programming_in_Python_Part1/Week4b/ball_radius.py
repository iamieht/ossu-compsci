# Ball radius control - version 1

import simplegui

WIDTH = 300
HEIGHT = 200
ball_radius = 50
BALL_RADIUS_INC = 3

# Handler for keydown
def keydown(key):
    global ball_radius
    
    if key == simplegui.KEY_MAP['down']:
        if ball_radius > BALL_RADIUS_INC:
            ball_radius -= BALL_RADIUS_INC
    elif key == simplegui.KEY_MAP['up']:
        ball_radius += BALL_RADIUS_INC

# Handler to draw on canvas
def draw(canvas):
    # note that CodeSkulptor throws an error if radius is not positive
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], ball_radius, 1, "White", "White")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
