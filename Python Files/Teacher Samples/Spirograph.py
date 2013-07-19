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

# Create Starburst Pattern
for i in range(180):    # repeat the following 180 times
    #### Add random color ####
    pen1.color(random.random(),
               random.random(),
               random.random())
    pen1.forward(125)
    pen1.back(125)
    polygon(pen1, 5, 100)
    pen1.right(2)
