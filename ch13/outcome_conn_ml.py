import pickle
from random import choice

# Define the simulate() function to play a complete game
def simulate():
    occupied = [list(),list(),list(),list(),list(),list(),list()]
    validinputs = [1,2,3,4,5,6,7]
    # Define a horizontal4() function to check connecting 4 horizontally
    def horizontal4(x, y, color, board):
        win = False
        for dif in (-3, -2, -1, 0):
            try:
                if board[x+dif][y] == color\
                and board[x+dif+1][y] == color\
                and board[x+dif+2][y] == color\
                and board[x+dif+3][y] == color\
                and  x+dif >=  0:
                    win = True            
            except IndexError:
                pass
        return win     
    # Define a vertical4() function to check connecting 4 vertically
    def vertical4(x, y, color, board):
        win = False
        try:
            if board[x][y] == color\
            and board[x][y-1] == color\
            and board[x][y-2] == color\
            and board[x][y-3] == color\
            and y-3 >=  0:
                win = True     
        except IndexError:
            pass
        return win   
    # Define a forward4() function to check connecting 4 diagonally in / shape
    def forward4(x, y, color, board):
        win = False
        for dif in (-3, -2, -1, 0):
            try:
                if board[x+dif][y+dif] == color\
                and board[x+dif+1][y+dif+1] == color\
                and board[x+dif+2][y+dif+2] == color\
                and board[x+dif+3][y+dif+3] == color\
                and x+dif >=  0 and y+dif >=  0:
                    win = True            
            except IndexError:
                pass
        return win     
    # Define a back4() function to check connecting 4 diagonally in \ shape
    def back4(x, y, color, board):
        win = False
        for dif in (-3, -2, -1, 0):
            try:
                if board[x+dif][y-dif] == color\
                and board[x+dif+1][y-dif-1] == color\
                and board[x+dif+2][y-dif-2] == color\
                and board[x+dif+3][y-dif-3] == color\
                and x+dif >=  0 and y-dif-3 >=  0:
                    win = True            
            except IndexError:
                pass
        return win       
    # Define a win_game() function to check if someone wins the game
    def win_game(num, color, board):
        win = False
        # Convert column and row numbers to indexes in the list of lists board
        x = num-1
        y = len(board[x])-1
        # Check all winning possibilities
        if vertical4(x, y, color, board) == True:
            win = True
        if horizontal4(x, y, color, board) == True:
            win = True
        if forward4(x, y, color, board) == True:
            win = True
        if back4(x, y, color, board) == True:
            win = True
        # Return the value stored in win
        return win
    # A history of moves made
    moves_made = []
    # Obtain game data
    with open('conn_simulates.pickle', 'rb') as fp:
        gamedata = pickle.load(fp)
    # Define the best_move() function
    def best_move():
        # Take column 4 in the first move
        if len(occupied[3]) == 0:
            return 4
        # If there is only one column has free slots, use the column
        if len(validinputs) == 1:
            return validinputs[0]
        simu = []
        for y in gamedata:
           if y[1:len(moves_made)+1] == moves_made:
               simu.append(y)
        # Now we look at the next move;           
        outcomes = {x:[] for x in validinputs} 
        # We collect all the outcomes for each next move
        for y in simu:
           outcomes[y[len(moves_made)+1]].append(y[0])
        # Set the initial value of bestoutcome        
        bestoutcome = -2;
        # Randomly select a move to be best_move
        best_move = validinputs[0]
        # iterate through all possible next moves 
        for move in validinputs:
            if len(outcomes[move])>0:
                outcome = sum(outcomes[move])/len(outcomes[move])
                # If the average outcome beats the current best
                if outcome>bestoutcome:
                    # Update the bestoutcome
                    bestoutcome = outcome
                    # Update the best move
                    best_move = move
        return best_move
    # The red player takes the first move    
    turn = "red"
    # Use winlose to record game outcome, default value is 0 (a tie)    
    winlose = [0]
    # Play a maximum of 42 steps (21 rounds)
    for i in range(21):
        # The player selects the best move
        col = best_move()
        if col == None:
            col = choice(validinputs)
        moves_made.append(col)
        # Add the move to the occupied list to keep track
        occupied[col-1].append(turn)
        
        # Check if the player has won
        if win_game(col, turn, occupied) == True:
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
        # The other player randomly selects a move
        col = choice(validinputs)
        moves_made.append(col)
        # Add the move to the occupied list to keep track
        occupied[col-1].append(turn)
        
        # Check if the player has won
        if win_game(col, turn, occupied) == True:
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
    return winlose+moves_made
# Repeat the game 1000 times and record all game outcomes
results = []        
for x in range(1000):
    result = simulate()
    results.append(result)    
with open('outcome_conn_ml.pickle', 'wb') as fp:
    pickle.dump(results,fp)
with open('outcome_conn_ml.pickle', 'rb') as fp:
    mylist = pickle.load(fp)    
winlose = [x[0] for x in mylist]
# Print out the number of winning games
print("the number of winning games is", winlose.count(1))
# Print out the number of tying games
print("the number of tying games is", winlose.count(0))
# Print out the number of losing games
print("the number of losing games is", winlose.count(-1))
