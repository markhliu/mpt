import turtle as t
from tkinter import messagebox
from random import choice
from copy import deepcopy

# Set up the screen
t.setup(600,600,10,70)
t.hideturtle()
t.tracer(False)
t.bgcolor("red")
t.title("Tic-Tac-Toe in Turtle Graphics")
# Draw horizontal lines and vertical lines to form grid
t.pensize(5)
for i in (-100,100):  
    t.up()
    t.goto(i,-300)
    t.down()
    t.goto(i,300)
    t.up()
    t.goto(-300,i)
    t.down()
    t.goto(300,i)
    t.up()
# Create a dictionary to map cell number to the cell center coordinates
cellcenter = {'1':(-200,-200), '2':(0,-200), '3':(200,-200),
            '4':(-200,0), '5':(0,0), '6':(200,0),
            '7':(-200,200), '8':(0,200), '9':(200,200)} 
# Go to the center of each cell, write down the cell number
for cell, center in list(cellcenter.items()):
    t.goto(center)
    t.write(cell,font = ('Arial',20,'normal'))
# The blue player moves first
turn = "blue"
# Count how many rounds played
rounds = 1
# Create a list of valid moves
validinputs = list(cellcenter.keys())
# Track the game board
occupied = {"blue":[],"white":[]}
# Define the win_game() function
def win_game(lst,color):
    win = False
    if '1' in lst[color] and '2' in lst[color] and '3' in lst[color]:
        win = True
    if '4' in lst[color] and '5' in lst[color] and '6' in lst[color]:
        win = True
    if '7' in lst[color] and '8' in lst[color] and '9' in lst[color]:
        win = True
    if '1' in lst[color] and '4' in lst[color] and '7' in lst[color]:
        win = True
    if '2' in lst[color] and '5' in lst[color] and '8' in lst[color]:
        win = True
    if '3' in lst[color] and '6' in lst[color] and '9' in lst[color]:
        win = True
    if '1' in lst[color] and '5' in lst[color] and '9' in lst[color]:
        win = True
    if '3' in lst[color] and '5' in lst[color] and '7' in lst[color]:
        win = True
    return win
# Define the best_move() function
def best_move():
    # Choose center at the first move
    if len(validinputs) == 9:
        return "5"
    # If there is only one move left, take it
    if len(validinputs) == 1:
        return validinputs[0]
    # Otherwise, see what will happen the next move hypothetically 
    valids = deepcopy(validinputs)
    winner = []
    # Go through all possible moves, and see if there is a winning move
    for move in valids:
        tooccupy = deepcopy(occupied)
        tooccupy['blue'].append(move)
        if win_game(tooccupy,'blue') == True:
            winner.append(move)        
    # If there is a winning move, take it
    if len(winner)>0:
        return winner[0]
    # If no winning move, look two steps ahead
    if len(winner) == 0 and len(validinputs) >= 2:
        # Check if your opponent has a winning move        
        for x in valids:
            for y in valids:
                if y != x:
                    tooccupy2 = deepcopy(occupied)
                    tooccupy2['blue'].append(x)
                    tooccupy2['white'].append(y)
                    if win_game(tooccupy2,'white') == True:
                        winner.append(y) 
        # If your opponent has a winnng move, block it                       
        if len(winner)>0:
            return winner[0]
def computer_move():
    global turn, rounds, validinputs
    # Choose the best move
    move = best_move()    
    # If no winning move, randomly choose
    if move == None:
        move = choice(validinputs) 
    # Go to the corresponding cell and place a dot of the player's color
    t.up()
    t.goto(cellcenter[move])
    t.dot(180,turn)
    t.update()
    # Add the move to the occupied list for the player
    occupied[turn].append(move)
    # Disallow the move in future rounds
    validinputs.remove(move)
    # Check if the player has won the game
    if win_game(occupied,turn) == True:
        # if a player wins, invalid all moves, end the game
        validinputs = []
        messagebox.showinfo("End Game",f"Congrats player {turn}, you won!")
    # If all cellls are occupied and no winner, it's a tie
    elif rounds == 9:
        messagebox.showinfo("Tie Game","Game over, it's a tie!")
    # Counting rounds
    rounds +=  1
    # Give the turn to the other player
    if turn == "blue":
        turn = "white"
    else:
        turn = "blue"    
# Computer moves first
computer_move()   
# Define a function mark_cell() to place a dot in the cell
def mark_cell(x,y):
    global turn, rounds, validinputs
    # Calculate the cell number based on x and y values
    if -300<x<300 and -300<y<300:
        col = int((x+500)//200)
        row = int((y+500)//200)
        cellnumber = str(col + (row - 1)*3)
    else:
        print('You have clicked outside the game board!')
    # If the move is a not valid one, show error message
    if cellnumber not in validinputs:
        messagebox.showerror("Error","Sorry, that's an invalid move!") 
    # If the move is valid, go ahead  
    else:
        # Go to the corresponding cell and place a dot of the player's color
        t.up()
        t.goto(cellcenter[cellnumber])
        t.dot(180,turn)
        t.update()
        # Add the move to the occupied list for the player
        occupied[turn].append(cellnumber)
        # Disallow the move in future rounds
        validinputs.remove(cellnumber)
        # Check if the player has won the game
        if win_game(occupied,turn) == True:
            # If a player wins, invalid all moves, end the game
            validinputs = []
            messagebox.showinfo("End Game",f"Congrats player {turn}, you won!")
        # If all cellls are occupied and no winner, it's a tie
        elif rounds == 9:
            messagebox.showinfo("Tie Game","Game over, it's a tie!")
        # Counting rounds
        rounds +=  1
        # Give the turn to the other player
        if turn == "blue":
            turn = "white"
        else:
            turn = "blue"   
        # Computer moves a move
        if len(validinputs)>0:
            computer_move()
# Bind the mouse click to the mark_cell() function
t.onscreenclick(mark_cell)
t.listen()    
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')
