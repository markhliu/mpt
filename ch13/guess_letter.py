import turtle as t
from random import choice

# Set up the board
t.setup(600,900)
t.hideturtle()
t.tracer(False)
t.bgcolor("azure")
t.title("A Hangman Game in Turtle Graphics")
# Draw the gallows
t.pensize(5)
t.pencolor("black")
t.up()
t.goto(0,220)
t.down()
t.goto(0,260)
t.goto(250,260)
t.goto(250,-300)
# Put incorrect guesses on top
t.up()
t.goto(-290,350)
t.write("incorrect guesses:",font=('Arial',20,'normal'))
# Put four empty spaces for the 4 letters at bottom
t.goto(-275,-400)
t.down()
t.goto(-175,-400)   
t.up()
t.goto(-125,-400)
t.down()
t.goto(-25,-400)   
t.up()
t.goto(25,-400)
t.down()
t.goto(125,-400)   
t.up()
t.goto(175,-400)
t.down()
t.goto(275,-400)   
t.up()
# Randomly pick one word
words=['that', 'with', 'have', 'this', 'will', 'your', 
       'from', 'they', 'know', 'want', 'been', 
       'good', 'much', 'some', 'time']
word=choice(words)
# Create a missed list
missed=[]
# Start the game loop
while True:
    # Take written input 
    inp=input("What's your choice?\n").lower()
    # Stop the loop if you key in "done"
    if inp=="done":
        break
    # Check if the picked letter is in the word, if yes, put it in the right position(s)
    elif inp in list(word):
        if inp==list(word)[0]:
            t.goto(-250,-390)
            t.write(inp,font=('Arial',60,'normal'))
        if inp==list(word)[1]:
            t.goto(-100,-390)
            t.write(inp,font=('Arial',60,'normal'))
        if inp==list(word)[2]:
            t.goto(40,-390)
            t.write(inp,font=('Arial',60,'normal'))
        if inp==list(word)[3]:
            t.goto(190,-390)
            t.write(inp,font=('Arial',60,'normal')) 
        continue
    # If the guessed letter is not in the word, show it at the top
    else:
        missed.append(inp)
        t.goto(-290+80*len(missed),260)
        t.write(inp,font=('Arial',60,'normal'))
        continue
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')

