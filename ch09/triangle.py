import turtle as t

t.Screen()
t.setup(600,500,100,200)
t.bgcolor('springgreen3')
t.title('Python Turtle Graphics')
t.hideturtle()
t.tracer(False)
t.pencolor('blue')
t.pensize(5)
t.up()
t.goto(-50,-50)
t.down()
t.goto(50,-50)
t.goto(0,100)
t.goto(-50,-50)
t.update()
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')
