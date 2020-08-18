# import needed modules
from turtle import *
from random import choice
from tkinter import messagebox

# make sure you put local modules in the same folder as this program
from mySAY import printAndSAY
from mysr import VTT

# set up the screen
Screen()
setup(600,600,100,200)
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
cellcenter={'1':(-200,-200), '2':(0,-200), '3':(200,-200),
            '4':(-200,0), '5':(0,0), '6':(200,0),
            '7':(-200,200), '8':(0,200), '9':(200,200)} 
# to to the center of each cell, write down the cell number
for cell, center in list(cellcenter.items()):
    goto(center)
    write(cell,font=('Arial',20,'normal'))
# The blue player moves first
turn="blue"
# count how many rounds played
rounds = 1
# create a list of valid moves
validinputs=list(cellcenter.keys())
# create a dictionary of moves made by each player
occupied={"blue":[],"white":[]}
# determine if a player has won the game
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
# start an infinite loop to take voice inputs
while True:
    # ask for your move
    printAndSAY(f"player {turn}, what's your move?")
    # capture your voice input
    inp=VTT()
    print(f"you said {inp}")
    inp=inp.replace('number ','')
    inp=inp.replace('one','1')   
    inp=inp.replace('two','2')
    inp=inp.replace('three','3')
    inp=inp.replace('four','4')
    inp=inp.replace('five','5')
    inp=inp.replace('six','6')
    inp=inp.replace('seven','7')
    inp=inp.replace('eight','8')
    inp=inp.replace('nine','9')
    if inp in validinputs:
        # go to the corresponding cell and place a dot of the player's color
        up()
        goto(cellcenter[inp])
        dot(180,turn)
        update()
        # add the move to the occupied list for the player
        occupied[turn].append(inp)
        # disallow the move in future rounds
        validinputs.remove(inp)
        # check if the player has won the game
        if WinGame()==True:
            # if a player wins, invalid all moves, end the game
            validinputs=[]
            printAndSAY(f"Congrats player {turn}, you won!")
            messagebox.showinfo("End Game",f"Congrats player {turn}, you won!")
            break

        # if all cellls are occupied and no winner, it's a tie
        if rounds==9:
            printAndSAY("Tie Game","Game over, it's a tie!")
            messagebox.showinfo("Tie Game","Game over, it's a tie!")
            break

        # counting rounds
        rounds += 1
        # give the turn to the other player
        if turn=="blue":turn="white"
        else:turn="blue"  
        
        # the computer makes a random move
        inp=choice(validinputs)
        printAndSAY(f'the computer occupies cell {inp}')
        up()
        goto(cellcenter[inp])
        dot(180,turn)
        update()
        occupied[turn].append(inp)
        validinputs.remove(inp)
        if WinGame()==True:
            validinputs=[]
            messagebox.showinfo("End Game",f"Congrats player {turn}, you won!")
            printAndSAY(f"Congrats player {turn}, you won!")
            break
        if rounds==9:
            messagebox.showinfo("Tie Game","Game over, it's a tie!")
            printAndSAY("Tie Game","Game over, it's a tie!")
            break
        rounds += 1
        if turn=="blue":turn="white"
        else:turn="blue"     

    # if the move is not a valid move, remind the player 
    else:
        printAndSAY("Sorry, that's an invalid move!")    
done()        
try:
    bye()
except Terminator:
    pass
