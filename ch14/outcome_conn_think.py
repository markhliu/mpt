import pickle
from random import choice
from copy import deepcopy

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

    # Define the validmoves() function to ensure three future moves 
    # will not cause any column to have more than six dics in it 
    def validmoves(m1,m2,m3,occupied):
        validmove = False
        if m1 == m2 == m3 and len(occupied[m1-1]) <= 3:
            validmove = True
        if m1 == m2 and m2 != m3 and len(occupied[m1-1]) <= 4:
            validmove = True
        if m1 == m3 and m2 != m3 and len(occupied[m1-1]) <= 4:
            validmove = True
        if m3 == m2 and m2 != m1 and len(occupied[m3-1]) <= 4:
            validmove = True
        return validmove
    # Define the best_move() function
    def best_move():
        # Take column 4 in the first move
        if len(occupied[3]) == 0:
            return 4
        # If only one column has free slots, take it
        if len(validinputs) == 1:
            return validinputs[0]
        # Otherwise, see what will happen the next move hypothetically 
        winner = []
        # Go through all possible moves, and see if there is a winning move
        for move in validinputs:
            tooccupy = deepcopy(occupied)
            tooccupy[move-1].append('red')
            if win_game(move,'red',tooccupy) == True:
                winner.append(move)        
        # If there is a winning move, take it
        if len(winner)>0:
                return winner[0]  
        # If no winning move, look two steps ahead
        if len(winner) == 0 and len(validinputs) >= 2:
            loser = []
            # Check if your opponent has a winning move        
            for m1 in validinputs:
                for m2 in validinputs:
                    if m2 != m1:
                        tooccupy = deepcopy(occupied)
                        tooccupy[m1-1].append('red')
                        tooccupy[m2-1].append('yellow')
                        if win_game(m2, 'yellow',tooccupy) == True:
                            winner.append(m2) 
                    if m2 == m1 and len(occupied[m1-1]) <= 4:
                        tooccupy2 = deepcopy(occupied)
                        tooccupy2[m1-1].append('red')
                        tooccupy2[m2-1].append('yellow')                    
                        if win_game(m2,'yellow',tooccupy2) == True:
                            loser.append(m2) 
            # If your opponent has a winnng move, block it                       
            if len(winner)>0:
                return winner[0]
            # If you can make a move to help your opponent to win, avoid it
            if len(loser)>0:
                myvalids = deepcopy(validinputs)
                for i in range(len(loser)):
                    myvalids.remove(loser[i])
                if len(myvalids)>0:
                    return choice(myvalids)        
            # Otherwise, look 3 moves ahead
            if len(winner) == 0 and len(loser) == 0:
                # Look at all possible combinations of 3 moves ahead
                for m1 in validinputs:
                    for m2 in validinputs:
                        for m3 in validinputs:
                            if validmoves(m1,m2,m3,occupied) == True: 
                                tooccupy3 = deepcopy(occupied)
                                tooccupy3[m1-1].append('red')
                                tooccupy3[m2-1].append('yellow')
                                tooccupy3[m3-1].append('red')
                                if win_game(m3, 'red', tooccupy3) == True:
                                    winner.append(m1)                        
                # See if there is a move now that can lead to winning in 3 moves
                if len(winner)>0:
                    cnt = {winner.count(x):x for x in winner}
                    maxcnt = sorted(cnt.keys())[-1]
                    return cnt[maxcnt]

    # The red player takes the first move    
    turn = "red"
    # Keep track of all intermediate moves
    moves_made = []
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
with open('outcome_conn_think.pickle', 'wb') as fp:
    pickle.dump(results,fp)
with open('outcome_conn_think.pickle', 'rb') as fp:
    mylist = pickle.load(fp)    
winlose = [x[0] for x in mylist]
# Print out the number of winning games
print("the number of winning games is", winlose.count(1))
# Print out the number of tying games
print("the number of tying games is", winlose.count(0))
# Print out the number of losing games
print("the number of losing games is", winlose.count(-1))
