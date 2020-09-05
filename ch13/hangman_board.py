import turtle as t

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
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')

