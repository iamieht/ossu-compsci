# "Stopwatch: The Game"
import simplegui
# define global variables
time = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = (t // 600)
    b = (t // 100) % 6
    c = (t % 100) // 10
    d = (t % 100) % 10    
    return str(a) + ":" + str(b) + str(c) + "." + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    timer.stop()

def reset():
    global time
    time = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [60, 160], 72, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 300)

# create timer
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 50)
frame.add_button("Stop", stop, 50)
frame.add_button("Reset", reset, 50)

# start frame & timer
frame.start()

