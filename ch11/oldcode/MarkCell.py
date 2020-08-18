# import all functions from the turtle module
from turtle import *

# set up the screen
Screen()
setup(600,600)
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
for cell, center in list(cellcenter.items()):
    goto(center)
    write(cell,font=('Arial',20,'normal'))
# The blue player moves first
turn="blue"
# define a function MarkCell() to place a dot in the cell
def MarkCell(x,y):
    # make the variable turn a globale variable
    global turn
    # Calculate the cell number based on x and y values
    if -300<x<300 and -300<y<300:
        col = int((x+500)//200)
        row = int((y+500)//200)
        # the cell number is a string varibale
        cellnumber = str(col + (row - 1)*3)
    else:
        print('you have clicked outside the game board')
    # go to the corresponding cell and place a dot of the player's color
    up()
    goto(cellcenter[cellnumber])
    dot(180,turn)
    update()
    # give the turn to the other player
    if turn=="blue":turn="white"
    else:turn="blue"       
# bind the mouse click to the MarkCell() function
onscreenclick(MarkCell)
listen()    
done()
try:
    bye()
except Terminator:
    pass
