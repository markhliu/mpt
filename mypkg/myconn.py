from turtle import *
from time import sleep
from random import choice
from copy import deepcopy

# Add the one-level-up directory to the search space
import sys
sys.path.append('../')

# Import functions from the local package
from mypkg.mysr import voice_to_text
from mypkg.mysay import print_say

def conn():
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
    # Define the smart_computer() function
    def smart_computer():
        if turn=="red":
            nonturn="yellow"
        else:
            nonturn="red"
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
            if win_game(move,turn,occupied)==True:
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
                        tooccupy[x-1].append(turn)
                        if win_game(y, nonturn,tooccupy)==True:
                            winner.append(y) 
                    if y==x and len(occupied[x-1])<=4:
                        tooccupy2=deepcopy(occupied)
                        tooccupy2[x-1].append(turn)
                        if win_game(y,nonturn,tooccupy2)==True:
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
            #otherwise, look 3 moves ahead
            if len(winner)==0 and len(loser)==0:
                #look at all possible combinations of 3 moves ahead
                for x in validinputs:
                    for y in validinputs:
                        for z in validinputs:
                            if (x==y==z and len(occupied[x-1])<=3) or (x==y and y!=z and len(occupied[x-1])<=4) or (x==z and y!=z and len(occupied[x-1])<=4) or (z==y and y!=x and len(occupied[z-1])<=4):
                                tooccupy3=deepcopy(occupied)
                                tooccupy3[x-1].append(turn)
                                tooccupy3[y-1].append(nonturn)
                                if win_game(z, turn, tooccupy3)==True:
                                    winner.append(x)                        
                #see if there is a move now that can lead to winning in 3 moves
                #if yes, take the value in winner that appears most often
                if len(winner)>0:
                    cnt={winner.count(x):x for x in winner}
                    maxcnt=sorted(cnt.keys())[-1]
                    return cnt[maxcnt]
    # Obtain move from a human player
    def person():
        print_say(f"Player {turn}, what's your move?")
        return voice_to_text().lower()
    # Obtain a move from a simple computer
    def simple_computer():
        return choice(validinputs)
    # Ask you for your choice of opponent
    while True:
        print_say("Do you want your opponent to be a person, a simple computer, or a smart computer?")
        which_player=voice_to_text().lower()
        print_say(f"You said {which_player}.")
        if 'person' in which_player:
            player=person
            break
        elif 'simple' in which_player:
            player=simple_computer
            break
        elif 'smart' in which_player:
            player=smart_computer
            break
    # Ask if you want to play first or second
    while True:
        print_say("Do you want to play first or second?")
        preference=voice_to_text().lower()
        print_say(f"You said {preference}.")
        if 'first' in preference:
            preference=1
            break
        elif 'second' in preference:
            preference=2
            break
   # Start game loop 
    while True:
        # See whose turn to play
        if (preference+rounds)%2==0:
            print_say(f"Player {turn}, what's your move?")
            inp=voice_to_text().lower()
        else:
            inp=player()
            if inp==None:
                inp=choice(validinputs)
        print_say(f"Player {turn} chooses {inp}.")
        try:
            inp=inp.replace('number ','')
            inp=inp.replace('one','1')   
            inp=inp.replace('two','2')
            inp=inp.replace('three','3')
            inp=inp.replace('four','4')
            inp=inp.replace('five','5')
            inp=inp.replace('six','6')
            inp=inp.replace('seven','7')
        except:
                pass
        # See if input is valid
        try:
            if int(inp) in validinputs:
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
                if win_game(col, turn, occupied)==True:
                    # If a player wins, invalid all moves, end the game
                    validinputs=[]
                    print_say(f"Congrats player {turn}, you won!")
                    break
                # If all cellls are occupied and no winner, it's a tie
                if rounds==42:
                    print_say("Game over, it's a tie!")
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
        # If inp is not a valid move, try again
        except:
            print_say("Sorry, that's an invalid move!")    
    try:
        bye()
    except Terminator:
        pass

