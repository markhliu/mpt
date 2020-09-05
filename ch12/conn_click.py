import turtle as t
from time import sleep
from tkinter import messagebox

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
    if col in validinputs:
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
        if win_game(col, row, turn)==True:
            # If a player wins, invalid all moves, end the game
            validinputs=[]
            messagebox.showinfo("End Game",f"Congrats player {turn}, you won!")
        # If all cellls are occupied and no winner, it's a tie
        elif rounds==42:
            messagebox.showinfo("Tie Game","Game over, it's a tie!")
        # Counting rounds
        rounds += 1
        # Add the move to the occupied list to keep track
        occupied[col-1].append(turn)
        # Update the list of valid moves
        if len(occupied[col-1])==6:
            validinputs.remove(col)
        # Give the turn to the other player
        if turn=="red":
            turn="yellow"
        else:
            turn="red"     
    # If col is not a valid move, show error message
    else:
        messagebox.showerror("Error","Sorry, that's an invalid move!")    
# Bind the mouse click to the conn() function
t.onscreenclick(conn)
t.listen()    
t.done()        
try:
    t.bye()
except t.Terminator:
    print('exit turtle')
