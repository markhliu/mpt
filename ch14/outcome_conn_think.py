import pickle
from random import choice
from copy import deepcopy

# Define the simulate() function to play a complete game
def simulate():
    occupied=[list(),list(),list(),list(),list(),list(),list()]
    validinputs=[1,2,3,4,5,6,7]
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
            #otherwise, look 3 moves ahead
            if len(winner)==0 and len(loser)==0:
                #look at all possible combinations of 3 moves ahead
                for x in validinputs:
                    for y in validinputs:
                        for z in validinputs:
                            if (x==y==z and len(occupied[x-1])<=3) or (x==y and y!=z and len(occupied[x-1])<=4) or (x==z and y!=z and len(occupied[x-1])<=4) or (z==y and y!=x and len(occupied[z-1])<=4):
                                tooccupy3=deepcopy(occupied)
                                tooccupy3[x-1].append('red')
                                tooccupy3[y-1].append('yellow')
                                if win_game(z, 'red', tooccupy3)==True:
                                    winner.append(x)                        
                #see if there is a move now that can lead to winning in 3 moves
                #if yes, take the value in winner that appears most often
                if len(winner)>0:
                    cnt={winner.count(x):x for x in winner}
                    maxcnt=sorted(cnt.keys())[-1]
                    return cnt[maxcnt]
    # The red player takes the first move    
    turn="red"
    # Keep track of all intermediate moves
    moves_made=[]
    winlose=[0]
    # Play a maximum of 42 steps (21 rounds)
    for i in range(21):
        # The player selects the best move
        col=best_move()
        if col==None:
            col=choice(validinputs)
        moves_made.append(col)
        # Check if the player has won
        if win_game(col, turn, occupied)==True:
            if turn=='red':
                winlose[0]=1
            if turn=='yellow':
                winlose[0]=-1
            break
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
        # The other player randomly selects a move
        col=choice(validinputs)
        moves_made.append(col)
        # Check if the player has won
        if win_game(col, turn, occupied)==True:
            if turn=='red':
                winlose[0]=1
            if turn=='yellow':
                winlose[0]=-1
            break
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
    # Record both game outcome and intermediate steps        
    return winlose+moves_made
# Repeat the game 1000 times and record all game outcomes
results=[]        
for x in range(1000):
    result=simulate()
    results.append(result)    
with open('outcome_conn_think.pickle', 'wb') as fp:
    pickle.dump(results,fp)
with open('outcome_conn_think.pickle', 'rb') as fp:
    mylist=pickle.load(fp)    
winlose=[x[0] for x in mylist]
# Print out the number of winning games
print("the number of winning games is", winlose.count(1))
# Print out the number of tying games
print("the number of tying games is", winlose.count(0))
# Print out the number of losing games
print("the number of losing games is", winlose.count(-1))
