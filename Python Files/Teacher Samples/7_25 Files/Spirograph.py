# Spirograph.py
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

# Create 2 pens
pen1 = Pen()
pen2 = Pen()

# Set Random Pen colors
pen1.color( random.random(),
           random.random(),
           random.random() )
pen2.color( random.random(),
           random.random(),
           random.random() )

polygon(pen1, 9, 72)
polygon(pen2, 28, 25)
