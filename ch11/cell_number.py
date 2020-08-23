from turtle import *

# Set up the screen
Screen()
setup(600,600, 10, 70)
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
# Go to the center of each cell, write down the cell number
for cell, center in list(cellcenter.items()):
    goto(center)
    write(cell,font=('Arial',20,'normal'))
# Define a function CellNumber() to print out the cell number
def CellNumber(x,y):
    if -300<x<300 and -300<y<300:
        # Calculate the column number based on x value
        col = int((x+500)//200)
        print('column number is ', col)
        # Calculate the row number based on y value
        row = int((y+500)//200)
        print('row number is ', row)
        # Calculate the cell number based on col and row
        cellnumber = col + (row - 1)*3
        print('cell number is ', cellnumber)
    else:
        print('you have clicked outside the game board')
# Hide turtle so that you don't see the arrowhead        
hideturtle()
# Bind the mouse click to the CellNumber() function
onscreenclick(CellNumber)
listen()    
done()
try:
    bye()
except Terminator:
    pass