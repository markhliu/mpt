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
t.pencolor('red')
t.forward(200)
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')

