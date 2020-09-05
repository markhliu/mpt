from random import choice
import pickle

# Define a simulate() function to generate a complete game
def simulate():
    occupied=[list(),list(),list(),list(),list(),list(),list()]
    validinputs=[1,2,3,4,5,6,7]
    def win_game(col, row, turn):
        win=False
        # Convert column and row numbers to indexes in the list occupied
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
    # The red player takes the first move    
    turn="red"
    # Keep track of all intermediate moves
    moves=[]
    # Use winlose to record game outcome, default value is 0 (a tie)
    winlose=[0]
    # Play a maximum of 42 steps
    for i in range(42):
        # The player randomly selects a move
        col=choice(validinputs)
        row=len(occupied[col-1])+1
        moves.append(col)
        # Check if the player has won
        if win_game(col, row, turn)==True:
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
    return winlose+moves
# Simulate the game 1 million times and record all games
results=[]        
for x in range(1000000):
    result=simulate()
    results.append(result)    
# Save the simulation data on your computer
with open('conn_simulates.pickle', 'wb') as fp:
    pickle.dump(results,fp)
# Read the data and print out the first 10 games       
with open('conn_simulates.pickle', 'rb') as fp:
    mylist=pickle.load(fp)
print(mylist[0:10])
