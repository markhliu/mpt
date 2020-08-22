from turtle import *

# Set up the screen
Screen()
setup(600,600)
hideturtle()
tracer(False)
bgcolor("red")
title("Tic-Tac-Toe in Turtle Graphics")
# Draw horizontal lines and vertical lines to form grid
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
# Create a dictionary to map cell number to the cell center coordinates
cellcenter={'1':(-200,-200), '2':(0,-200), '3':(200,-200),
            '4':(-200,0), '5':(0,0), '6':(200,0),
            '7':(-200,200), '8':(0,200), '9':(200,200)} 
# Create a dictionary to map cell number to the cell center coordinates
for cell, center in list(cellcenter.items()):
    goto(center)
    write(cell,font=('Arial',20,'normal'))
# The blue player moves first
turn="blue"
# Define a function mark_cell() to place a dot in the cell
def mark_cell(x,y):
    # Make the variable turn a globale variable
    global turn
    # Calculate the cell number based on x and y values
    if -300<x<300 and -300<y<300:
        col = int((x+500)//200)
        row = int((y+500)//200)
        # The cell number is a string varibale
        cellnumber = str(col + (row - 1)*3)
    else:
        print('you have clicked outside the game board')
    # Go to the corresponding cell and place a dot of the player's color
    up()
    goto(cellcenter[cellnumber])
    dot(180,turn)
    update()
    # Give the turn to the other player
    if turn=="blue":turn="white"
    else:turn="blue"       
# Bind the mouse click to the mark_cell() function
onscreenclick(mark_cell)
listen()    
done()
try:
    bye()
except Terminator:
    pass
