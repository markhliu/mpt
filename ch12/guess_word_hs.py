import turtle as t
from random import choice
from tkinter import messagebox
from tkinter import PhotoImage

# Import functions from the local package
from mptpkg import voice_to_text, print_say

# Set up the board
t.setup(600,500)
t.hideturtle()
t.tracer(False)
t.bgcolor("lavender")
t.title("Guess the Word Game in Turtle Graphics")
# Define a variable to count how many guesses left
score = 6
# Create a second turtle to show guesses left
left = t.Turtle()
left.up()
left.hideturtle()
left.goto(-290,200)
left.write(f"guesses left:   {score}", font = ('Arial',20,'normal'))
# Put incorrect guesses on top
t.up()
t.goto(-290,150)
t.write("incorrect guesses:", font = ('Arial',20,'normal'))
# Put four empty spaces for the four letters at bottom
for x in range(4):
    t.goto(-275+150*x,-200)
    t.down()
    t.goto(-175+150*x,-200)   
    t.up()
t.update()
# Put words in a dictionary and randomly pick one
words = ['that', 'with', 'have', 'this', 'will', 'your', 
   'from', 'they', 'know', 'want', 'been', 
   'good', 'much', 'some', 'time']
word = choice(words)
# Create a missed list
missed = []
# Load a picture of the coin to the script
coin = PhotoImage(file = "cash.png").subsample(10,10)
t.addshape("coin", t.Shape("image", coin))
# Create six coin on screen 
coins = [0]*6
for i in range(6):
    coins[i] = t.Turtle('coin')
    coins[i].up()
    coins[i].goto(-100+50*i,0)
t.update()
# Prepare the validinputs and gotright lists
validinputs = list('abcdefghijklmnopqrstuvwxyz')
gotright = []
# Start the game loop
while True:
    # Ask for your move
    print_say("What's your guess?")
    # Capture your voice input
    inp = voice_to_text().lower()
    print_say(f"you said {inp}")
    inp = inp.replace('letter ','')
    # Say "stop listening" or press CTRL+C to stop the game
    if inp == "stop listening":
        break
    # If the letter is not a valid input, remind
    elif inp not in validinputs:
        print_say("Sorry, that's an invalid input!")
    # Otherwise, go ahead with the game
    else:  
        # Check if the letter is in the word
        if inp in list(word):
            # If yes, put it in the right position(s)
            for w in range(4):
                if inp == list(word)[w]:
                    t.goto(-250+150*w,-190)
                    t.write(inp, font = ('Arial',60,'normal'))
                    gotright.append(inp)
            # If got four positions right, the player wins
            if len(gotright) == 4:
                print_say("Great job, you got the word right!")
                messagebox.showinfo\
                ("End Game","Great job, you got the word right!")
                break
        # If the letter is not in the word, show it at the top
        else:
            # Reduce guesses left by 1
            score -=  1
            # Remove a coin
            coins[-(6-score)].hideturtle()
            # Update the number of guesses left on board
            left.clear()
            left.write\
            (f"guesses left:   {score}", font = ('Arial',20,'normal'))
            t.update()            
            missed.append(inp)
            t.goto(-290+80*len(missed),60)
            t.write(inp, font = ('Arial',60,'normal'))
            if len(missed) == 6:
                # If all six changes are used up, end game
                print_say("Sorry, you used up all your six guesses!")
                messagebox.showinfo\
                ("End Game","Sorry, you used up all your six guesses!")
                break 
        # Remove the letter from the validinputs list
        validinputs.remove(inp)       
    # Update everything that happens in the iteration
    t.update()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')
