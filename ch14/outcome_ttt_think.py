import pickle
from random import choice
from copy import deepcopy

def simulate():
    validinputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    occupied = {"blue":[],"white":[]}
    def win_game(lst,color):
        win = False
        if '1' in lst[color] and '2' in lst[color] and '3' in lst[color]:
            win = True
        if '4' in lst[color] and '5' in lst[color] and '6' in lst[color]:
            win = True
        if '7' in lst[color] and '8' in lst[color] and '9' in lst[color]:
            win = True
        if '1' in lst[color] and '4' in lst[color] and '7' in lst[color]:
            win = True
        if '2' in lst[color] and '5' in lst[color] and '8' in lst[color]:
            win = True
        if '3' in lst[color] and '6' in lst[color] and '9' in lst[color]:
            win = True
        if '1' in lst[color] and '5' in lst[color] and '9' in lst[color]:
            win = True
        if '3' in lst[color] and '5' in lst[color] and '7' in lst[color]:
            win = True
        return win
    turn = "blue"
    i = 0
    # Define the best_move() function
    def best_move():
        # Choose center at the first move
        if len(validinputs) == 9:
            return "5"
        # If there is only one move left, take it
        if len(validinputs) == 1:
            return validinputs[0]
        # Otherwise, see what will happen the next move hypothetically 
        valids = deepcopy(validinputs)
        winner = []
        # Go through all possible moves, and see if there is a winning move
        for move in valids:
            tooccupy = deepcopy(occupied)
            tooccupy['blue'].append(move)
            if win_game(tooccupy,'blue') == True:
                winner.append(move)        
        # If there is a winning move, take it
        if len(winner)>0:
            return winner[0]
        # If no winning move, look two steps ahead
        if len(winner) == 0 and len(validinputs) >= 2:
            # Check if your opponent has a winning move        
            for x in valids:
                for y in valids:
                    if y != x:
                        tooccupy2 = deepcopy(occupied)
                        tooccupy2['blue'].append(x)
                        tooccupy2['white'].append(y)
                        if win_game(tooccupy2,'white') == True:
                            winner.append(y) 
            # If your opponent has a winnng move, block it                       
            if len(winner)>0:
                return winner[0]
            # Otherwise, look 3 moves ahead
            if len(winner) == 0 and len(validinputs) >= 3:
                # Look at all possible combinations of 3 moves ahead
                for x in valids:
                    for y in valids:
                        if y != x:
                            for z in valids:
                                if z != x and z != y:
                                    tooccupy3 = deepcopy(occupied)
                                    tooccupy3['blue'].append(x)
                                    tooccupy3['white'].append(y)
                                    tooccupy3['blue'].append(z)
                                    if win_game(tooccupy3,'blue') == True:
                                        winner.append(x)                        
                if len(winner)>0:
                    cnt = {winner.count(x):x for x in winner}
                    maxcnt = sorted(cnt.keys())[-1]
                    return cnt[maxcnt]
            
           
    moves_made = []
    winlose = [0]
    while True:
        inp = best_move()
        if inp == None:
            inp = choice(validinputs)
        occupied[turn].append(inp)
        validinputs.remove(inp)
        moves_made.append(inp)
        if win_game(occupied,turn) == True:
            winlose[0] = 1
            break
        if i == 8:
            break  
        if turn == "blue":
            turn = "white"
        else:
            turn = "blue"               
        i += 1
        inp = choice(validinputs)
        occupied[turn].append(inp)
        validinputs.remove(inp)
        moves_made.append(inp)
        if win_game(occupied,turn) == True:
            winlose[0] = -1
            break
        if turn == "blue":
            turn = "white"
        else:
            turn = "blue"               
        i += 1
    return winlose+moves_made
# Repeat the game 1000 times and record all game outcomes
results = []        
for x in range(1000):
    result = simulate()
    results.append(result)    
with open('outcome_ttt_think.pickle', 'wb') as fp:
    pickle.dump(results,fp)  
with open('outcome_ttt_think.pickle', 'rb') as fp:
    mylist = pickle.load(fp)    
winlose = [x[0] for x in mylist]
print("the number of winning games is", winlose.count(1))
print("the number of tying games is", winlose.count(0))
print("the number of losing games is", winlose.count(-1))

    