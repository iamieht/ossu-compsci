# "Stopwatch: The Game"
import simplegui
# define global variables
time = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"


# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1
    print time

# define draw handler

    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 300)

# create timer
timer = simplegui.create_timer(10, tick)
# register event handlers


# start frame & timer
frame.start()
timer.start()

# Please remember to review the grading rubric
