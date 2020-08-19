from turtle import *
from time import sleep
from tkinter import messagebox

# Add the one-level-up directory to the search space
import sys
sys.path.append('../')

# Import functions from the loacal package
from mypkg.mysr import voice_to_text
from mypkg.mysay import print_say

# Set up the screen
Screen()
setup(700,600)
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
# Draw five thin grey horizontal lines to form grid    
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
# Creae a list of valid moves
validinputs=['1','2','3','4','5','6','7']
# Define a win_game() function to check if someone wins the game
def win_game(col, row, turn):
    win=False
    # Convert column and row numbers to indexes in the list of lists occupied
    x=col-1
    y=row-1
    # Check if the disc forms four in a row vertically
    try:
        if occupied[x][y-1]==turn and occupied[x][y-2]==turn and occupied[x][y-3]==turn and y>=3:
                win=True     
    except IndexError:
                pass                
    # Check if the disc forms four in a row horizontally
    try:
        if occupied[x-3][y]==turn and occupied[x-2][y]==turn and occupied[x-1][y]==turn and x>=3:
                win=True            
    except IndexError:
                pass
    try:
        if occupied[x-2][y]==turn and occupied[x-1][y]==turn and occupied[x+1][y]==turn and x>=2:
                win=True            
    except IndexError:
                pass
    try:
        if occupied[x-1][y]==turn and occupied[x+1][y]==turn and occupied[x+2][y]==turn and x>=1:
                win=True          
    except IndexError:
                pass
    try:
        if occupied[x+1][y]==turn and occupied[x+2][y]==turn and occupied[x+3][y]==turn:
                win=True        
    except IndexError:
                pass
    # Check if the disc forms four in a row diagonally in / shape
    try:
        if occupied[x+1][y+1]==turn and occupied[x+2][y+2]==turn and occupied[x+3][y+3]==turn:
                win=True       
    except IndexError:
                pass
    try:
        if occupied[x-1][y-1]==turn and occupied[x+1][y+1]==turn and occupied[x+2][y+2]==turn  and x>=1 and y>=1:
                win=True      
    except IndexError:
                pass
    try:     
        if occupied[x-1][y-1]==turn and occupied[x-2][y-2]==turn and occupied[x+1][y+1]==turn  and x>=2 and y>=2:
                win=True
    except IndexError:
                pass
    try:
        if occupied[x-1][y-1]==turn and occupied[x-2][y-2]==turn and occupied[x-3][y-3]==turn  and x>=3 and y>=3:
                win=True      
    except IndexError:
                pass
    # Check if the disc forms four in a row diagonally in \ shape
    try:
        if occupied[x+1][y-1]==turn and occupied[x+2][y-2]==turn and occupied[x+3][y-3]==turn and y>=3:
                win=True         
    except IndexError:
                pass
    try:
        if occupied[x-1][y+1]==turn and occupied[x+1][y-1]==turn and occupied[x+2][y-2]==turn and x>=1 and y>=2:
                win=True      
    except IndexError:
                pass
    try:
        if occupied[x-1][y+1]==turn and occupied[x-2][y+2]==turn and occupied[x+1][y-1]==turn and x>=1 and y>=1:
                win=True      
    except IndexError:
                pass
    try:
        if occupied[x-1][y+1]==turn and occupied[x-2][y+2]==turn and occupied[x-3][y+3]==turn  and x>=3:
                win=True        
    except IndexError:
                pass
    # Return the value stored in win
    return win
# Count the number of rounds
rounds=1
# Start an infinite loop to take voice inputs
while True:
    # Ask for your move
    print_say(f"Player {turn}, what's your move?")
    # Capture your voice input
    inp=voice_to_text().lower()
    print_say(f"You said {inp}.")
    inp=inp.replace('number ','')
    inp=inp.replace('one','1')   
    inp=inp.replace('two','2')
    inp=inp.replace('three','3')
    inp=inp.replace('four','4')
    inp=inp.replace('five','5')
    inp=inp.replace('six','6')
    inp=inp.replace('seven','7')
    # If col is not a valid move, try again
    if inp not in validinputs:
        print_say("Sorry, that's an invalid move!")    
    # If your voice input is a valid column number, play the move
    else:
        col=int(inp)
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
        update()
        # Check if the player has won
        if win_game(col, row, turn)==True:
            # If a player wins, invalid all moves, end the game
            validinputs=[]
            print_say(f"Congrats player {turn}, you won!")
            messagebox.showinfo("End Game",f"Congrats player {turn}, you won!")
            break
        # If all cellls are occupied and no winner, it's a tie
        if rounds==42:
            print_say("Game over, it's a tie!")
            messagebox.showinfo("Tie Game","Game over, it's a tie!")
            break
        # Counting rounds
        rounds += 1
        # Add the move to the occupied list to keep track
        occupied[col-1].append(turn)
        # Update the list of valid moves
        if len(occupied[col-1])==6:
            validinputs.remove(str(col))        
        # Give the turn to the other player
        if turn=="red":
            turn="yellow"
        else:
            turn="red" 
        # The computer randomly selects a move
        if len(validinputs)>0:
            col=int(choice(validinputs))
        print_say(f'The computer chooses column {col}.')
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
        update()
        # Check if the player has won
        if win_game(col, row, turn)==True:
            # If a player wins, invalid all moves, end the game
            validinputs=[]
            print_say(f"Congrats player {turn}, you won!")
            messagebox.showinfo("End Game",f"Congrats player {turn}, you won!")
            break
        # If all cellls are occupied and no winner, it's a tie
        if rounds==42:
            print_say("Game over, it's a tie!")
            messagebox.showinfo("Tie Game","Game over, it's a tie!")
            break
        # Counting rounds
        rounds += 1
        # Add the move to the occupied list to keep track
        occupied[col-1].append(turn)
        # Update the list of valid moves
        if len(occupied[col-1])==6:
            validinputs.remove(str(col))        
        # Give the turn to the other player
        if turn=="red":
            turn="yellow"
        else:
            turn="red"        
done()
try:
    bye()
except Terminator:
    pass
