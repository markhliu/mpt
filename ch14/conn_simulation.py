from random import choice
import pickle

# Define a simulate() function to generate a complete game
def simulate():
    occupied = [list(),list(),list(),list(),list(),list(),list()]
    validinputs = [1,2,3,4,5,6,7]
    # Define a horizontal4() function to check connecting 4 horizontally
    def horizontal4(x, y, turn):
        win = False
        for dif in (-3, -2, -1, 0):
            try:
                if occupied[x+dif][y] == turn\
                and occupied[x+dif+1][y] == turn\
                and occupied[x+dif+2][y] == turn\
                and occupied[x+dif+3][y] == turn\
                and  x+dif >= 0:
                    win = True            
            except IndexError:
                pass
        return win     
    # Define a vertical4() function to check connecting 4 vertically
    def vertical4(x, y, turn):
        win = False
        try:
            if occupied[x][y] == turn\
            and occupied[x][y-1] == turn\
            and occupied[x][y-2] == turn\
            and occupied[x][y-3] == turn\
            and y-3 >= 0:
                win = True     
        except IndexError:
            pass
        return win   
    # Define a forward4() function to check connecting 4 diagonally in / shape
    def forward4(x, y, turn):
        win = False
        for dif in (-3, -2, -1, 0):
            try:
                if occupied[x+dif][y+dif] == turn\
                and occupied[x+dif+1][y+dif+1] == turn\
                and occupied[x+dif+2][y+dif+2] == turn\
                and occupied[x+dif+3][y+dif+3] == turn\
                and x+dif >=  0 and y+dif >= 0:
                    win = True            
            except IndexError:
                pass
        return win     
    # Define a back4() function to check connecting 4 diagonally in \ shape
    def back4(x, y, turn):
        win = False
        for dif in (-3, -2, -1, 0):
            try:
                if occupied[x+dif][y-dif] == turn\
                and occupied[x+dif+1][y-dif-1] == turn\
                and occupied[x+dif+2][y-dif-2] == turn\
                and occupied[x+dif+3][y-dif-3] == turn\
                and x+dif >=  0 and y-dif-3 >= 0:
                    win = True            
            except IndexError:
                pass
        return win     
    # Define a win_game() function to check if someone wins the game
    def win_game(col, row, turn):
        win = False
        # Convert column and row numbers to list indexes
        x = col-1
        y = row-1
        # Check all winning possibilities
        if vertical4(x, y, turn) == True:
            win = True
        if horizontal4(x, y, turn) == True:
            win = True
        if forward4(x, y, turn) == True:
            win = True
        if back4(x, y, turn) == True:
            win = True
        # Return the value stored in win
        return win
    # The red player takes the first move    
    turn = "red"
    # Keep track of all intermediate moves
    moves = []
    # Use winlose to record game outcome, default value is 0 (a tie)
    winlose = [0]
    # Play a maximum of 42 steps
    for i in range(42):
        # The player randomly selects a move
        col = choice(validinputs)
        row = len(occupied[col-1])+1
        moves.append(col)
        # Add the move to the occupied list to keep track
        occupied[col-1].append(turn)        
        # Check if the player has won
        if win_game(col, row, turn) == True:
            if turn == 'red':
                winlose[0] = 1
            if turn == 'yellow':
                winlose[0] = -1
            break
        # Update the list of valid moves
        if len(occupied[col-1]) == 6 and col in validinputs:
            validinputs.remove(col)        
        # Give the turn to the other player
        if turn == "red":
            turn = "yellow"
        else:
            turn = "red"     
    # Record both game outcome and intermediate steps        
    return winlose+moves
# Simulate the game 1 million times and record all games
results = []        
for x in range(1000000):
    result = simulate()
    results.append(result)    
# Save the simulation data on your computer
with open('conn_simulates.pickle', 'wb') as fp:
    pickle.dump(results,fp)
# Read the data and print out the first 10 games       
with open('conn_simulates.pickle', 'rb') as fp:
    mylist = pickle.load(fp)
print(mylist[0:10])
