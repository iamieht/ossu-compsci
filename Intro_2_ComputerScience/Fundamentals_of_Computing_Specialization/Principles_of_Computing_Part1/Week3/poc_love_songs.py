"""
Love pop song generator
Credit to Antonio - IIPP - spring 2013
"""

import random

def print_first_verse():
    """
    Print first verse
    """
    choice = random.randrange(0,4)
    if choice == 0:
        print "In this lonely afternoon"
    elif choice == 1:
        print "In this sunny Sunday morning"
    elif choice == 2:
        print "In this dark and cold winter"
    elif choice == 3:
        print "Under this magic summer night sky"

def print_second_verse():
    """
    Print second verse
    """
    choice = random.randrange(0,4)
    if choice == 0:
        print "I walk alone, trying to forget you,"
    elif choice == 1:
        print "I try not to see your name anywhere,"
    elif choice == 2:
        print "I can't do anything but think of you,"
    elif choice == 3:
        print "I'm writing a love letter to you,"

def print_third_verse():
    """
    Print third verse
    """
    choice = random.randrange(0,4)
    if choice == 0:
        print "Even if the rain will fall"
    elif choice == 1:
        print "Even if you don't share my passion for Lord Fener"
    elif choice == 2:
        print "Even if I've loved your sister more than you"
    elif choice == 3:
        print "Even if your dad tries to kill me everyday"

def print_fourth_verse():
    """
    Print third verse
    """
    choice = random.randrange(0, 4)
    if choice == 0:
        print "One day we'll run away together"
    elif choice == 1:
        print "One day we'll share a common dream"
    elif choice == 2:
        print "I'll do anything for you"
    elif choice == 3:
        print "I'll fix your broken windshield wiper"

    
def feat_pitbull(riff):
    """
    Print riff by Pitbull
    """
    if riff == 0:
        print "TUNZ TUNZ TUNZ TUNZ (Pitbull)"
        print " "
  
def print_stanza():
    """
    Print a stanze
    """
    print_first_verse()
    print_second_verse()
    print_third_verse()
    print_fourth_verse()
    print "Because I love you, babe"
    print "Because I love you, babe"
    print " "

def print_love_song():
    """
    Print a random love song
    """
    riff = random.randrange(0,2)
    print_stanza()
    print_stanza()
    feat_pitbull(riff)
    print_stanza()
    print "(Sweet music, time slows down)"
    print " "
    print "Because I love you, babe"
    print "Because I love you, babe"

print_love_song()