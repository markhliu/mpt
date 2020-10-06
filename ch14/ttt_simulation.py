from random import choice
import pickle

# Define a simulate() function to generate a complete game
def simulate():
    validinputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    occupied = {"blue":[],"white":[]}
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
    # The blue player  takes the first move    
    turn = "blue"
    # Keep track of all intermediate moves
    moves = []
    # Use winlose to record game outcome, default value is 0 (a tie)
    winlose = [0]
    # Play a maximum of nine steps
    for i in range(9):
        # The player randomly selects a move
        inp = choice(validinputs)
        # Recrod what's on board to determine win or lose
        occupied[turn].append(inp)
        # Remove a cell once it's occupied
        validinputs.remove(inp)
        # Record the move
        moves.append(inp)
        # Check if a player has won
        if win_game() == True:
            if turn == 'blue':
                winlose[0] = 1
            if turn == 'white':
                winlose[0] = -1
            break 
        # Change turns
        if turn == "blue":
            turn = "white"
        else:
            turn = "blue"               
    # Record both game outcome and intermediate steps        
    return winlose+moves
# Simulate the game 1 million times and record all games
results = []        
for x in range(1000000):
    result = simulate()
    results.append(result)    
# Save the simulation data on your computer
with open('ttt_simulates.pickle', 'wb') as fp:
    pickle.dump(results,fp)
# Read the data and print out the first 10 games       
with open('ttt_simulates.pickle', 'rb') as fp:
    mylist = pickle.load(fp)
print(mylist[0:10])
