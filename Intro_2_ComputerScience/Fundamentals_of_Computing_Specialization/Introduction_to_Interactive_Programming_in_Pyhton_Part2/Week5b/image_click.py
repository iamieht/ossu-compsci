# Image positioning problem

###################################################
# Student should enter code below

import simplegui

# global constants
WIDTH = 400
HEIGHT = 300

# load test image
test_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png")

# image dimesions
image_size = (95,93)

# image_pos
image_pos = [WIDTH//2,HEIGHT//2]

# mouseclick handler
def click(pos):
    image_pos[0] = pos[0]
    image_pos[1] = pos[1]
    
# draw handler
def draw(canvas):
    canvas.draw_image(test_image, (image_size[0]//2, image_size[1]//2), image_size, image_pos, image_size)

    
# create frame and register draw handler    
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)


# start frame
frame.start()
        
                                       