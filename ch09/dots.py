import turtle as t

t.Screen()
t.setup(600,500,100,200)
t.bgcolor('lightgreen')
t.title('Python Turtle Graphics')
t.up()
t.goto(150,100)
t.dot(120,'red')
t.goto(-150,100)
t.dot(135,'yellow')
t.goto(150,-100)
t.dot(125,'blue')
t.goto(-150,-100)
t.dot(140,'green')
t.hideturtle()
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')
