# Ball grid slution

###################################################
# Student should enter code below

import simplegui

BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS


# define draw
def draw(canvas):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            canvas.draw_circle((2*BALL_RADIUS*x+BALL_RADIUS, 2*BALL_RADIUS*y+BALL_RADIUS), BALL_RADIUS, 5, 'Green')
                      
# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# start frame
frame.start()


