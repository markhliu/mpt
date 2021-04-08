import turtle as t

# Set up the screen   
t.Screen()
t.setup(810,710, 10, 70)
t.hideturtle()
t.tracer(False)
t.bgcolor('lightgreen')
# Draw the vertical lines to create 7 columns
t.pensize(5)
for i in range(-350,400,100):  
    t.up()
    t.goto(i, -298)
    t.down()
    t.goto(i, 303)
    t.up()
# Draw the horizontal lines to separate the screen in 6 rows
t.pensize(1)
t.color('gray')
for i in range(-300,400,101):  
    t.up()
    t.goto(-350,i)
    t.down()
    t.goto(350,i)
    t.up()   
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')
