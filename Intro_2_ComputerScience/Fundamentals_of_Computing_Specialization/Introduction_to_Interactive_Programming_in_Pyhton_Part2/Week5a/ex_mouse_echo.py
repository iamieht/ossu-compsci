# Echo mouse click in console

###################################################
# Student should enter code below
import simplegui

def click(pos):
    print 'Mouse click at', pos
    
frame = simplegui.create_frame('Mouse Echo', 200, 200)
frame.set_mouseclick_handler(click)
frame.start()




###################################################
# Sample output

#Mouse click at (104, 105)
#Mouse click at (169, 175)
#Mouse click at (197, 135)
#Mouse click at (176, 111)
#Mouse click at (121, 101)
#Mouse click at (166, 208)
#Mouse click at (257, 235)
#Mouse click at (255, 235)