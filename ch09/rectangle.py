import turtle as t

# Set up the screen
t.Screen()
t.setup(600,500,100,200)
t.bgcolor('green')
t.title('Python Turtle Graphics')
t.hideturtle()
t.tracer(False)
t.pensize(6)
# Draw the first side
t.forward(200)
t.left(90)
# Draw the second side
t.forward(100)
t.left(90)
# Draw the third side
t.forward(200)
t.left(90)
# Finish the rectangle
t.forward(100)
t.update()
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')
