# MyTurtleTest.py

# import statements
import random
from turtle import *

# Create pens
pen1 = Pen()
pen2 = Pen()
pen3 = Pen()

#### Add color ####
# with keyword
pen1.color("purple")

# with hex code (http://colorsontheweb.com/colorwizard.asp)
pen2.color("#0CA3F4")

# a random color using rgb (red, green, blue)
# random.random() creates a number between 0 and .9999999
pen3.color(random.random(),
           random.random(),
           random.random())

# Draw some lines
pen3.fd(300)

# Pen 1 will draw a square

pen1.up() # lift pen up
pen1.goto(-200, 200) # move pen
pen1.down() # put the pen back down

pen1.fd(100)
pen1.right(90)
pen1.fd(100)
pen1.right(90)
pen1.fd(100)
pen1.right(90)
pen1.fd(100)

# Pen 2 will use a for loop to draw a square
for i in range(4):
    pen2.forward(60)
    pen2.right(90)



