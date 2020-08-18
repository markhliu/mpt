# import all functions from the turtle module
from turtle import *

# set up the screen
Screen()
setup(600,600, 10, 70)
hideturtle()
tracer(False)
bgcolor("red")
title("Tic-Tac-Toe in Turtle Graphics")
# draw horizontal lines and vertical lines to form grid
pensize(5)
for i in (-100,100):  
    up()
    goto(i, -300)
    down()
    goto(i, 300)
    up()
    goto(-300,i)
    down()
    goto(300,i)
    up()
# create a dictionary to map cell number to the cell center coordinates
cellcenter={'1':(-200,-200), '2':(0,-200), '3':(200,-200),
            '4':(-200,0), '5':(0,0), '6':(200,0),
            '7':(-200,200), '8':(0,200), '9':(200,200)} 
# to to the center of each cell, write down the cell number
for cell, center in list(cellcenter.items()):
    goto(center)
    write(cell,font=('Arial',20,'normal'))
done()
try:
    bye()
except Terminator:
    pass
