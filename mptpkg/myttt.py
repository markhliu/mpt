import turtle as t
from random import choice
from copy import deepcopy

from mptpkg import voice_to_text, print_say

def ttt():
    t.setup(600,600,100,200)
    t.hideturtle()
    t.tracer(False)
    t.bgcolor("red")
    t.title("Tic-Tac-Toe in Turtle Graphics")
    # Draw horizontal lines and vertical lines to form grid
    t.pensize(5)
    for i in (-100,100):  
        t.up()
        t.goto(i, -300)
        t.down()
        t.goto(i, 300)
        t.up()
        t.goto(-300,i)
        t.down()
        t.goto(300,i)
        t.up()
    # Create a dictionary to map cell number to the cell center coordinates
    cellcenter = {'1':(-200,-200), '2':(0,-200), '3':(200,-200),
                '4':(-200,0), '5':(0,0), '6':(200,0),
                '7':(-200,200), '8':(0,200), '9':(200,200)} 
    # Go to the center of each cell, write down the cell number
    for cell, center in list(cellcenter.items()):
        t.goto(center)
        t.write(cell,font = ('Arial',20,'normal'))
    # The blue player moves first
    turn = "blue"
    # Count how many rounds played
    rounds = 1
    # Create a list of valid moves
    validinputs = list(cellcenter.keys())
    # Track the game board
    occupied = {"blue":[],"white":[]}
    # Define the win_game() function
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
    # Define the smart_computer() function
    def smart_computer():
        if turn == "blue":
            nonturn = "white"
        else:
            nonturn = "blue"
        # Choose center at the first move
        if "5" in validinputs:
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
            tooccupy[turn].append(move)
            if win_game(tooccupy,turn) == True:
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
                        tooccupy2[turn].append(x)
                        tooccupy2[nonturn].append(y)
                        if win_game(tooccupy2,nonturn) == True:
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
                                    tooccupy3[turn].append(x)
                                    tooccupy3[nonturn].append(y)
                                    tooccupy3[turn].append(z)
                                    if win_game(tooccupy3,turn) == True:
                                        winner.append(x)                        
                if len(winner)>0:
                    cnt = {winner.count(x):x for x in winner}
                    maxcnt = sorted(cnt.keys())[-1]
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
        print_say('''Do you want your opponent to be a person,
        a simple computer, or a smart computer?''')
        which_player = voice_to_text().lower()
        print_say(f"You said {which_player}.")
        if 'person' in which_player:
            player = person
            break
        elif 'simple' in which_player:
            player = simple_computer
            break
        elif 'smart' in which_player:
            player = smart_computer
            break
    # Ask if you want to play first or second
    while True:
        print_say("Do you want to play first or second?")
        preference = voice_to_text().lower()
        print_say(f"You said {preference}.")
        if 'first' in preference:
            preference = 1
            break
        elif 'second' in preference:
            preference = 2
            break

    # Add a dictionary of words to replace
    to_replace = {'number ':'', 'cell ':'', 'column ':'',
                  'one':'1', 'two':'2', 'three':'3',
                  'four':'4', 'for':'4', 'five':'5',
                  'six':'6', 'seven':'7', 'eight':'8','nine':'9'} 

   # Start game loop 
    while True:
        # See whose turn to play
        if (preference+rounds)%2 == 0:
            print_say(f"Player {turn}, what's your move?")
            inp = voice_to_text().lower()
        else:
            inp = player()
            if inp == None:
                inp = choice(validinputs)
        print_say(f"Player {turn} chooses {inp}.")
        for x in list(to_replace.keys()):   
            inp = inp.replace(x, to_replace[x])
        # If the move is a not valid one, remind
        if inp not in validinputs:
            print_say("Sorry, that's an invalid move!") 
        # If the move is valid, go ahead  
        else:
            # Go to the corresponding cell and place a dot of the player's color
            t.up()
            t.goto(cellcenter[inp])
            t.dot(180,turn)
            t.update()
            # Add the move to the occupied list for the player
            occupied[turn].append(inp)
            # Disallow the move in future rounds
            validinputs.remove(inp)
            # Check if the player has won the game
            if win_game(occupied,turn) == True:
                # If a player wins, invalid all moves, end the game
                validinputs = []
                print_say(f"Congrats player {turn}, you won!")
                break
            # If all cellls are occupied and no winner, it's a tie
            elif rounds == 9:
                print_say("Game over, it's a tie!")
                break
            # Counting rounds
            rounds += 1
            # Give the turn to the other player
            if turn == "blue":
                turn = "white"
            else:
                turn = "blue"   
    try:
        t.bye()
    except t.Terminator:
        print('exit turtle')
