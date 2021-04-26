import pickle

validinputs = [1,2,3,4,5,6,7]
# A game history
moves_made = [4,5,4,5,4,5]
# The game board
occupied = [list(),list(),list(),
            ['red','red','red'],
            ['yellow','yellow','yellow'],
            list(),list()]
# Obtain gamedata
with open('conn_simulates.pickle', 'rb') as fp:
    gamedata = pickle.load(fp)
simu = []
for y in gamedata:
   if y[1:len(moves_made)+1] == moves_made:
       simu.append(y)
# Now we look at the next move           
outcomes = {x:[] for x in validinputs} 
# We collect all the outcomes for each next move
for y in simu:
   outcomes[y[len(moves_made)+1]].append(y[0])
print(outcomes)   
# Set the initial value of bestoutcome        
bestoutcome = -2;
# Randomly select a move to be best_move
best_move = validinputs[0]
# Iterate through all possible next moves 
for move in validinputs:
    if len(outcomes[move])>0:
        outcome = sum(outcomes[move])/len(outcomes[move])
        print\
        (f'when the next move is {move}, the average outcome is {outcome}')
        # If the average outcome beats the current best
        if outcome>bestoutcome:
            # Update the bestoutcome
            bestoutcome = outcome
            #update the best move
            best_move = move
print(f'the best next move is {best_move}')
