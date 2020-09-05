import turtle as t
from time import sleep
from tkinter import messagebox
from random import choice
from copy import deepcopy

# Set up the screen
t.setup(700,600, 10, 70)
t.hideturtle()
t.tracer(False)
t.bgcolor("lightgreen")
t.title("Connect Four in Turtle Graphics")
# Draw six thick vertical lines
t.pensize(5)
for i in range(-250,350,100):  
    t.up()
    t.goto(i, -350)
    t.down()
    t.goto(i, 350)
    t.up()
# Draw five thin gray horizontal lines to form grid    
t.pensize(1)
t.pencolor("grey")
for i in range(-200,300,100):  
    t.up()
    t.goto(-350,i)
    t.down()
    t.goto(350,i)
    t.up()
# Write column numbers on the board
colnum=1
for x in range(-300, 350, 100):
    t.goto(x,270)
    t.write(colnum,font=('Arial',20,'normal'))
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
fall=t.Turtle()
fall.up()
fall.hideturtle()
# Create a list of valid moves
validinputs=[1,2,3,4,5,6,7]
# Define a win_game() function to check if someone wins the game
def win_game(num, color, lst):
    win=False
    # Convert column and row numbers to indexes in the list of lists lst
    x=num-1
    y=len(lst[x])
    # Check if the disc forms four in a row vertically
    try:
        if lst[x][y-1]==color and lst[x][y-2]==color and lst[x][y-3]==color and y>=3:
                win=True     
    except IndexError:
        pass  
    # Check if the disc forms four in a row horizontally
    try:
        if lst[x-3][y]==color and lst[x-2][y]==color and lst[x-1][y]==color and x>=3:
                win=True            
    except IndexError:
        pass
    try:
        if lst[x-2][y]==color and lst[x-1][y]==color and lst[x+1][y]==color and x>=2:
                win=True            
    except IndexError:
        pass
    try:
        if lst[x-1][y]==color and lst[x+1][y]==color and lst[x+2][y]==color and x>=1:
                win=True          
    except IndexError:
        pass
    try:
        if lst[x+1][y]==color and lst[x+2][y]==color and lst[x+3][y]==color:
                win=True        
    except IndexError:
        pass
    # Check if the disc forms four in a row diagonally in / shape
    try:
        if lst[x+1][y+1]==color and lst[x+2][y+2]==color and lst[x+3][y+3]==color:
                win=True       
    except IndexError:
        pass
    try:
        if lst[x-1][y-1]==color and lst[x+1][y+1]==color and lst[x+2][y+2]==color  and x>=1 and y>=1:
                win=True      
    except IndexError:
        pass
    try:     
        if lst[x-1][y-1]==color and lst[x-2][y-2]==color and lst[x+1][y+1]==color  and x>=2 and y>=2:
                win=True
    except IndexError:
        pass
    try:
        if lst[x-1][y-1]==color and lst[x-2][y-2]==color and lst[x-3][y-3]==color  and x>=3 and y>=3:
                win=True      
    except IndexError:
        pass
    # Check if the disc forms four in a row diagonally in \ shape
    try:
        if lst[x+1][y-1]==color and lst[x+2][y-2]==color and lst[x+3][y-3]==color and y>=3:
                win=True         
    except IndexError:
        pass
    try:
        if lst[x-1][y+1]==color and lst[x+1][y-1]==color and lst[x+2][y-2]==color and x>=1 and y>=2:
                win=True      
    except IndexError:
        pass
    try:
        if lst[x-1][y+1]==color and lst[x-2][y+2]==color and lst[x+1][y-1]==color and x>=1 and y>=1:
                win=True      
    except IndexError:
        pass
    try:
        if lst[x-1][y+1]==color and lst[x-2][y+2]==color and lst[x-3][y+3]==color  and x>=3:
                win=True        
    except IndexError:
        pass
    # Return the value stored in win
    return win
# Count the number of rounds
rounds=1
# Define the best_move() function
def best_move():
    # Take column 4 in the first move
    if len(occupied[3])==0:
        return 4
    # If only one column has free slots, take it
    if len(validinputs)==1:
        return validinputs[0]
    # Otherwise, see what will happen the next move hypothetically 
    winner=[]
    # Go through all possible moves, and see if there is a winning move
    for move in validinputs:
        if win_game(move,'red',occupied)==True:
            winner.append(move)        
    # If there is a winning move, take it
    if len(winner)>0:
            return winner[0] 
    # If no winning move, look two steps ahead
    if len(winner)==0 and len(validinputs)>=2:
        loser=[]
        # Check if your opponent has a winning move        
        for x in validinputs:
            for y in validinputs:
                if y!=x:
                    tooccupy=deepcopy(occupied)
                    tooccupy[x-1].append('red')
                    if win_game(y, 'yellow',tooccupy)==True:
                        winner.append(y) 
                if y==x and len(occupied[x-1])<=4:
                    tooccupy2=deepcopy(occupied)
                    tooccupy2[x-1].append('red')
                    if win_game(y,'yellow',tooccupy2)==True:
                        loser.append(y) 
        # If your opponent has a winnng move, block it                       
        if len(winner)>0:
            return winner[0]
        # If you can make a move to help your opponent to win, avoid it
        if len(loser)>0:
            myvalids=deepcopy(validinputs)
            for i in range(len(loser)):
                myvalids.remove(loser[i])
            if len(myvalids)>0:
                return choice(myvalids)
def computer_move():
    global turn, rounds, validinputs
    # Choose the best move
    col = best_move()
    if col==None:
        col = choice(validinputs)
    # Calculate the lowest available row number in that column
    row=1+len(occupied[col-1])
    # Show the disc fall from the top
    if row<6:
        for i in range(6,row,-1):
            fall.goto(xs[col-1],ys[i-1])
            fall.dot(80,turn)
            t.update()
            sleep(0.05)
            fall.clear()
    # Go to the cell and place a dot of the player's color
    t.up()
    t.goto(xs[col-1],ys[row-1])
    t.dot(80,turn)
    t.update()
    # Check if the player has won
    if win_game(col, turn, occupied)==True:
        # If a player wins, invalid all moves, end the game
        validinputs=[]
        messagebox.showinfo("End Game",f"Congrats player {turn}, you won!")
    # If all cellls are occupied and no winner, it's a tie
    if rounds==42 and win_game(col, turn, occupied)==False:
        messagebox.showinfo("Tie Game","Game over, it's a tie!")
    # Counting rounds
    rounds += 1
    # Add the move to the occupied list to keep track
    occupied[col-1].append(turn)
    # Update the list of valid moves
    if len(occupied[col-1])==6 and col in validinputs:
        validinputs.remove(col)        
    # Give the turn to the other player
    if turn=="red":
        turn="yellow"
    else:
        turn="red"     
# Computer moves first
computer_move()
# Define a function conn() to place a disc in a cell
def conn(x,y):
    # Declare global variables
    global turn, rounds, validinputs
    # Calculate the column number based on x and y values
    if -350<x<350 and -300<y<300:
        col = int((x+450)//100)
    else:
        print('You have clicked outside the game board!')
    # Check if it's a valid move
    if col not in validinputs:
        messagebox.showerror("Error","Sorry, that's an invalid move!")    
    else:
        # Calculate the lowest available row number in that column
        row=len(occupied[col-1])+1
        # Show the disc fall from the top
        if row<6:
            for i in range(6,row,-1):
                fall.goto(xs[col-1],ys[i-1])
                fall.dot(80,turn)
                t.update()
                sleep(0.05)
                fall.clear()
        # Go to the cell and place a dot of the player's color
        t.up()
        t.goto(xs[col-1],ys[row-1])
        t.dot(80,turn)
        t.update
        # Check if the player has won
        if win_game(col, turn, occupied)==True:
            # If a player wins, invalid all moves, end the game
            validinputs=[]
            messagebox.showinfo("End Game",f"Congrats player {turn}, you won!")
        # If all cells are occupied and no winner, it's a tie
        elif rounds==42:
            messagebox.showinfo("Tie Game","Game over, it's a tie!")
        # Counting rounds
        rounds += 1
        # Add the move to the occupied list to keep track
        occupied[col-1].append(turn)
        # Update the list of valid moves
        if len(occupied[col-1])==6 and col in validinputs:
            validinputs.remove(col)
        # Give the turn to the other player
        if turn=="red":
            turn="yellow"
        else:
            turn="red"     
        # Computer moves next
        if len(validinputs)>0:
            computer_move()
# Bind the mouse click to the conn() function
t.onscreenclick(conn)
t.listen()    
t.done()        
try:
    t.bye()
except t.Terminator:
    print('exit turtle')
