import pickle
from random import choice

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
    # A history of moves moade
    moves_made = []
    with open('ttt_simulates.pickle', 'rb') as fp:
        gamedata = pickle.load(fp)
    def best_move():
        if len(moves_made) == 0:
            return "5"
        if len(moves_made) == 8:
            return validinputs[0]
        else:
            simu = []
            for y in gamedata:
               if y[1:len(moves_made)+1] == moves_made:
                   simu.append(y)          
            outcomes = {x:[] for x in validinputs} 
            for y in simu:
               outcomes[y[len(moves_made)+1]].append(y[0])        
            Bestoutcome = -2;
            best_move = validinputs[0]
            for move in validinputs:
                if len(outcomes[move])>0:
                    outcome = sum(outcomes[move])/len(outcomes[move])
                    if outcome>Bestoutcome:
                        Bestoutcome = outcome
                        best_move = move
            return best_move

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
with open('outcome_ttt_ml.pickle', 'wb') as fp:
    pickle.dump(results,fp)        
with open('outcome_ttt_ml.pickle', 'rb') as fp:
    mylist = pickle.load(fp)    
winlose = [x[0] for x in mylist]
print("the number of winning games is", winlose.count(1))
print("the number of tying games is", winlose.count(0))
print("the number of losing games is", winlose.count(-1))

    