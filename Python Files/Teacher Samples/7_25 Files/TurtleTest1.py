# TurtleTest1.py
# import libraries
from turtle import *
import random

# Create 2 pens
pen1 = Pen()
pen2 = Pen()

# Set Pen colors
pen1.color("green")
pen2.color("#336699") # '#336699' is a hex color code
                        # colorsontheweb.com
# Move the 2 pens
pen1.forward(150)
pen2.backward(150)
pen1.right(90)
pen1.forward(150)
pen2.left(45)
pen2.forward(200)

# Make a pattern with a for loop (25 times)
for i in range(25):
    pen2.backward(50)
    pen2.right(29)
    pen2.forward(14)
    
