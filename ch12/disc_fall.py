from turtle import *
from time import sleep

Screen()
setup(700, 600, 10, 70)
hideturtle()
tracer(False)
bgcolor("lightgreen")
title("Connect Four in Turtle Graphics")
# Draw six thick vertical lines
pensize(5)
for i in range(-250,350,100):  
    up()
    goto(i, -350)
    down()
    goto(i, 350)
    up()
# Draw five thin gray horizontal lines to form grid    
pensize(1)
pencolor("grey")
for i in range(-200,300,100):  
    up()
    goto(-350,i)
    down()
    goto(350,i)
    up()
# Write column numbers on the board
colnum=1
for x in range(-300, 350, 100):
    goto(x,270)
    write(colnum,font=('Arial',20,'normal'))
    colnum += 1
# The red player moves first
turn="red"
# The x-coordinates of the center of the 7 columns
xs=[-300,-200,-100,0,100,200,300]
# The y-coordinates of the center of the 6 rows
ys=[-250,-150,-50,50,150,250]
# Keep track of the occupied cells
occupied=[list(),list(),list(),list(),list(),list(),list()]
# Create a second turtle to show disc falling
fall=Turtle()
fall.up()
fall.hideturtle()
# Define a function conn() to place a disc in a cell
def conn(x,y):
    # Make the variable turn a globale variable
    global turn
    # Calculate the column number based on x and y values
    if -350<x<350 and -300<y<300:
        col = int((x+450)//100)
    else:
        print('You have clicked outside the game board!')
    # Calculate the lowest available row number in that column
    row=len(occupied[col-1])+1
    # Show the disc fall from the top
    if row<6:
        for i in range(6,row,-1):
            fall.goto(xs[col-1],ys[i-1])
            fall.dot(80,turn)
            update()
            sleep(0.05)
            fall.clear()
    # Go to the cell and place a dot of the player's color
    up()
    goto(xs[col-1],ys[row-1])
    dot(80,turn)
    # Add the move to the occupied list to keep track
    occupied[col-1].append(turn)
    # Give the turn to the other player
    if turn=="red":
        turn="yellow"
    else:turn="red"     
# Bind the mouse click to the conn() function
onscreenclick(conn)
listen()    
done()
try:
    bye()
except Terminator:
    pass
