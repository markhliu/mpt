from turtle import *
from random import choice

# Set up the board
Screen()
setup(600,900)
hideturtle()
tracer(False)
bgcolor("azure")
title("A Hangman Game in Turtle Graphics")
# Draw the gallows
pensize(5)
pencolor("black")
up()
goto(0,220)
down()
goto(0,260)
goto(250,260)
goto(250,-300)
# Put incorrect guesses on top
up()
goto(-290,350)
write("incorrect guesses:",font=('Arial',20,'normal'))
# Put four empty spaces for the 4 letters at bottom
goto(-275,-400)
down()
goto(-175,-400)   
up()
goto(-125,-400)
down()
goto(-25,-400)   
up()
goto(25,-400)
down()
goto(125,-400)   
up()
goto(175,-400)
down()
goto(275,-400)   
up()
# Put the most common 4-letter words in a dictionary and randomly pick one
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
            goto(-250,-390)
            write(inp,font=('Arial',60,'normal'))
        if inp==list(word)[1]:
            goto(-100,-390)
            write(inp,font=('Arial',60,'normal'))
        if inp==list(word)[2]:
            goto(40,-390)
            write(inp,font=('Arial',60,'normal'))
        if inp==list(word)[3]:
            goto(190,-390)
            write(inp,font=('Arial',60,'normal')) 
        continue
    # If the guessed letter is not in the word, show it at the top
    else:
        missed.append(inp)
        goto(-290+80*len(missed),260)
        write(inp,font=('Arial',60,'normal'))
        continue
done()
try:
    bye()
except Terminator:
    pass
