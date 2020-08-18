# import all functions from the turtle module
from turtle import *

# set up the screen
Screen()
setup(620,620,360,100)
title("How Mouse-Clicks Work in Turtle Graphics")

# define a function GetXY() to print the x and y value of the point you click
def GetXY(x,y):
    print('x is ', x)
    print('y is ', y)
# hide turtle so that you don't see the arrowhead        
hideturtle()
# bind the mouse click to the GetXY() function
onscreenclick(GetXY)
listen()
done()
try:
    bye()
except Terminator:
    pass
