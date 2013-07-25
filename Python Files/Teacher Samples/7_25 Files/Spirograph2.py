# Spirograph2.py
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
    # Set Random Pen color
    pen1.color( random.random(),
               random.random(),
               random.random() )
    # Draw a polygon
    polygon(pen1, 9, 72)
    # Turn 2 degrees
    pen1.left(2)
