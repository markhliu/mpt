from turtle import *

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
done()
try:
    bye()
except Terminator:
    pass
