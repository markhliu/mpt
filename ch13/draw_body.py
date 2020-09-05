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
# Define the draw_head() function
def draw_head():
    t.up()
    t.goto(0,170)
    t.dot(120,"black")
# Define the draw_torso() function
def draw_torso():
    t.up()
    t.goto(0,100)
    t.down()
    t.goto(0,-100)
    t.up()
# Define the draw_left_arm() functiont.
def draw_left_arm():
    t.up()
    t.goto(0,100)
    t.down()
    t.goto(-100,-100)
    t.up()   
# Define the draw_right_arm() functiont.t.
def draw_right_arm():
    t.up()
    t.goto(0,100)
    t.down()
    t.goto(100,-100)
    t.up()   
# Define the draw_left_leg() functiont.t.
def draw_left_leg():
    t.up()
    t.goto(0,-100)
    t.down()
    t.goto(-100,-300)
    t.up()   
# Define the draw_right_leg() function 
def draw_right_leg():
    t.up()
    t.goto(0,-100)
    t.down()
    t.goto(100,-300)
    t.up()   
# Call the functions to draw the whole body
draw_head()
draw_torso()
draw_left_arm()
draw_right_arm()
draw_left_leg()
draw_right_leg()

t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')
