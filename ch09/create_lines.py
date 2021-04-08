import turtle as t

t.Screen()
t.setup(600,500,100,200)
t.bgcolor('lightgreen')
t.title('Python Turtle Graphics')
t.pensize(6)
t.goto(200,100)
t.up()
t.pencolor('blue')
for i in range(8):
    t.goto(-200+50*i,-150)
    t.down()
    t.goto(-200+50*i+30,-150)
    t.up()
t.hideturtle()
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')

