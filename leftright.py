import turtle as t

t.Screen()
t.setup(600,500,100,200)
t.bgcolor('light blue')
t.title('Python Turtle Graphics')
t.pensize(5)
t.right(30)
t.forward(200)
t.left(30)
t.backward(400)
t.left(90)
t.pencolor('orange')
t.forward(200)
t.pencolor('teal')
t.right(90)
t.forward(200)
t.pencolor('yellow')
t.right(90)
t.forward(100)
t.pencolor('blue')
t.left(90)
t.forward(30)
t.done()
try:
    t.bye()
except t.Terminator:
    pass

