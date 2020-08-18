from turtle import *

# Set up the screen
Screen()
setup(620,620,360,100)
title("How Mouse-Clicks Work in Turtle Graphics")
# Define a function GetXY() to print the x and y value of the point you click
def GetXY(x,y):
    print('x is ', x)
    print('y is ', y)
# Hide turtle so that you don't see the arrowhead        
hideturtle()
# Bind the mouse click to the GetXY() function
onscreenclick(GetXY)
listen()
done()
try:
    bye()
except Terminator:
    pass
