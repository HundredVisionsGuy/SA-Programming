# MyTurtleTest2.py
# A demonstration of loops and functions

# import statements
import random
from turtle import *

# Define a function
def polygon(pen, sides, length):
    """ makes a [sides] sided polygon each side is [length] long """
    for i in range(sides):
        pen.forward(length)
        pen.right( 360.0 / sides )

# Create pens
pen1 = Pen()
pen1.speed("fastest") # Speeded up the pen

# Create 10 random polygons in random locations
for i in range(40):    # repeat the following 180 times
    #### Add random color ####
    pen1.color(random.random(),
               random.random(),
               random.random())
    pen1.up() # lift up pen
    pen1.goto(random.randrange(-240, 240),
              random.randrange(-240, 240)) # go to random location
    pen1.down() # put pen down
    polygon(pen1, random.randrange(3, 15), 25) # draw random polygon
