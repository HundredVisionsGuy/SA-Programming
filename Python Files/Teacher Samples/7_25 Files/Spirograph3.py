# Spirograph3.py: the donut!
# import libraries
from turtle import *
import random

# Define Functions
def polygon(pen, sides, length):
    pen.begin_fill()
    for i in range(sides):
        pen.forward(length)
        pen.right( 360.0 / sides )
    pen.end_fill()

# Create pen
pen1 = Pen()
# Speed it up
pen1.speed('fastest')

# Make spirograph with a for loop (180 times)
for i in range(180):
    pen1.up() # lift up the pen (so it doesn't draw a line)
    pen1.forward(100)
    pen1.down() # Set down the pen (so we can draw the polygon)
    # Set Random Pen color
    pen1.color( random.random(),
               random.random(),
               random.random() )
    # Draw a polygon
    polygon(pen1, 9, 72)
    pen1.up()
    pen1.backward(100)
    # Turn 2 degrees
    pen1.left(2)
