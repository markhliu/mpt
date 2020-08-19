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
# Define the draw_head() function
def draw_head():
    up()
    goto(0,170)
    dot(120,"black")
# Define the draw_torso() function
def draw_torso():
    up()
    goto(0,100)
    down()
    goto(0,-100)
    up()
# Define the draw_left_arm() function    
def draw_left_arm():
    up()
    goto(0,100)
    down()
    goto(-100,-100)
    up()   
# Define the draw_right_arm() function        
def draw_right_arm():
    up()
    goto(0,100)
    down()
    goto(100,-100)
    up()   
# Define the draw_left_leg() function        
def draw_left_leg():
    up()
    goto(0,-100)
    down()
    goto(-100,-300)
    up()   
# Define the draw_right_leg() function 
def draw_right_leg():
    up()
    goto(0,-100)
    down()
    goto(100,-300)
    up()   
# Call the functions to draw the whole body
draw_head()
draw_torso()
draw_left_arm()
draw_right_arm()
draw_left_leg()
draw_right_leg()

done()
try:
    bye()
except Terminator:
    pass
