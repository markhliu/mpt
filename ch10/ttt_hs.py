import turtle as t
from random import choice
from tkinter import messagebox

# Import functions from the local package
from mptpkg import voice_to_text, print_say

# Set up the screen
t.setup(600,600,10,70)
t.tracer(False)
t.hideturtle()
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
# Create a dictionary of moves made by each player
occupied = {"blue":[],"white":[]}
# Determine if a player has won the game
def win_game():
    win = False
    if '1' in occupied[turn] and '2' in occupied[turn] and '3' in occupied[turn]:
        win = True
    if '4' in occupied[turn] and '5' in occupied[turn] and '6' in occupied[turn]:
        win = True
    if '7' in occupied[turn] and '8' in occupied[turn] and '9' in occupied[turn]:
        win = True
    if '1' in occupied[turn] and '4' in occupied[turn] and '7' in occupied[turn]:
        win = True
    if '2' in occupied[turn] and '5' in occupied[turn] and '8' in occupied[turn]:
        win = True
    if '3' in occupied[turn] and '6' in occupied[turn] and '9' in occupied[turn]:
        win = True
    if '1' in occupied[turn] and '5' in occupied[turn] and '9' in occupied[turn]:
        win = True
    if '3' in occupied[turn] and '5' in occupied[turn] and '7' in occupied[turn]:
        win = True
    return win
# Add a dictionary of words to replace
to_replace = {'number ':'', 'cell ':'',
              'one':'1', 'two':'2', 'three':'3',
              'four':'4', 'for':'4', 'five':'5',
              'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
# Start an infinite loop to take voice inputs
while True:
    # Ask for your move
    print_say(f"Player {turn}, what's your move?")
    # Capture your voice input
    inp = voice_to_text()
    print_say(f"You said {inp}.")
    for x in list(to_replace.keys()):   
        inp = inp.replace(x, to_replace[x])
    if inp in validinputs:
        # Go to the corresponding cell and place a dot of the player's color
        t.up()
        t.goto(cellcenter[inp])
        t.dot(180,turn)
        t.update()
        # Add the move to the occupied list for the player
        occupied[turn].append(inp)
        # Disallow the move in future rounds
        validinputs.remove(inp)
        # check if the player has won the game
        if win_game() == True:
            # if a player wins, invalid all moves, end the game
            validinputs = []
            print_say(f"Congrats player {turn}, you won!")
            messagebox.showinfo\
            ("End Game",f"Congrats player {turn}, you won!")
            break
        # If all cellls are occupied and no winner, it's a tie
        elif rounds == 9:
            print_say("Game over, it's a tie!")
            messagebox.showinfo("Tie Game","Game over, it's a tie!")
            break
        # Counting rounds
        rounds += 1
        # Give the turn to the other player
        if turn == "blue":
            turn = "white"
        else:
            turn = "blue"  
 
        # The computer makes a random move
        inp = choice(validinputs)
        print_say(f'The computer occupies cell {inp}.')
        t.up()
        t.goto(cellcenter[inp])
        t.dot(180,turn)
        t.update()
        occupied[turn].append(inp)
        validinputs.remove(inp)
        if win_game() == True:
            validinputs = []
            print_say(f"Congrats player {turn}, you won!")
            messagebox.showinfo\
            ("End Game",f"Congrats player {turn}, you won!")
            break
        elif rounds == 9:
            print_say("Game over, it's a tie!")
            messagebox.showinfo("Tie Game","Game over, it's a tie!")
            break
        rounds += 1
        if turn == "blue":
            turn = "white"
        else:
            turn = "blue"     

    # If the move is not a valid move, remind the player 
    else:
        print_say("Sorry, that's an invalid move!")    
t.done()        
try:
    t.bye()
except t.Terminator:
    print('exit turtle')

