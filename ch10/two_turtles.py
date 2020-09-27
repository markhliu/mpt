import turtle as t

# Set up the screent.
t.setup(810,710)
t.tracer(False)
t.hideturtle()
t.bgcolor('lightgreen')
t.color('blue')
t.pensize(5)
t.up()
t.goto(-200,-100)
t.down()
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)
t.left(90)
t.forward(400)
# Create a second turtle 
msg = t.Turtle()
msg.hideturtle()
msg.up()
msg.color('red')
msg.goto(0,-200)
msg.write('this is written by the second turtle', align = 'center', font = ('Arial',30,'normal'))
t.update()
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')



