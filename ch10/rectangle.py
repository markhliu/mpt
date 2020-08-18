from turtle import *

# Set up the screen
Screen()
setup(600,500,100,200)
bgcolor('green')
title('Python Turtle Graphics')
hideturtle()
tracer(False)
pensize(6)
# Draw the first side
forward(200)
left(90)
# Draw the second side
forward(100)
left(90)
# Draw the third side
forward(200)
left(90)
# Finish the rectangle
forward(100)
update()
done()
try:
    bye()
except Terminator:
    pass
