from tkinter import messagebox
from turtle import *

# Set up the screen
Screen()
setup(600,600,100,200)
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
# Go to the center of each cell, write down the cell number
for cell, center in list(cellcenter.items()):
    goto(center)
    write(cell,font=('Arial',20,'normal'))
# The blue player moves first
turn="blue"
# Count how many rounds played
rounds = 1
# Create a list of valid moves
validinputs=list(cellcenter.keys())
# Determine if a player has won the game
occupied={"blue":[],"white":[]}
# Determine if a player has won the game
def WinGame():
    win=False
    if '1' in occupied[turn] and '2' in occupied[turn] and '3' in occupied[turn]:
        win=True
    if '4' in occupied[turn] and '5' in occupied[turn] and '6' in occupied[turn]:
        win=True
    if '7' in occupied[turn] and '8' in occupied[turn] and '9' in occupied[turn]:
        win=True
    if '1' in occupied[turn] and '4' in occupied[turn] and '7' in occupied[turn]:
        win=True
    if '2' in occupied[turn] and '5' in occupied[turn] and '8' in occupied[turn]:
        win=True
    if '3' in occupied[turn] and '6' in occupied[turn] and '9' in occupied[turn]:
        win=True
    if '1' in occupied[turn] and '5' in occupied[turn] and '9' in occupied[turn]:
        win=True
    if '3' in occupied[turn] and '5' in occupied[turn] and '7' in occupied[turn]:
        win=True
    return win
# Define a function mark_cell() to place a dot in the cell
def mark_cell(x,y):
    global turn, rounds, validinputs
    # Calculate the cell number based on x and y values
    if -300<x<300 and -300<y<300:
        col = int((x+500)//200)
        row = int((y+500)//200)
        # The cell number is a string varibale
        cellnumber = str(col + (row - 1)*3)
    else:
        print('you have clicked outside the game board')
    # Check if the move is a valid one
    if cellnumber in validinputs:
        # Go to the corresponding cell and place a dot of the player's color
        up()
        goto(cellcenter[cellnumber])
        dot(180,turn)
        # Add the move to the occupied list for the player
        occupied[turn].append(cellnumber)
        # Disallow the move in future rounds
        validinputs.remove(cellnumber)
        # Check if the player has won the game
        if WinGame()==True:
            # If a player wins, invalid all moves, end the game
            validinputs=[]
            messagebox.showinfo("End Game",f"Congrats player {turn}, you won!")
        # If all cellls are occupied and no winner, it's a tie
        if rounds==9:
            messagebox.showinfo("Tie Game","Game over, it's a tie!")
        # Counting rounds
        rounds += 1
        # Give the turn to the other player
        if turn=="blue":turn="white"
        else:turn="blue"     
    # If the move is not a valid move, remind the player 
    else:
        messagebox.showerror("Error","Sorry, that's an invalid move!")    
# Bind the mouse click to the mark_cell() function
onscreenclick(mark_cell)
listen()    
done()
try:
    bye()
except Terminator:
    pass
