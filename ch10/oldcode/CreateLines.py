from turtle import *

Screen()
setup(600,500,100,200)
bgcolor('lightgreen')
title('Python Turtle Graphics')
pensize(6)
goto(200,100)
up()
pencolor('blue')
for i in range(8):
    goto(-200+50*i,-150)
    down()
    goto(-200+50*i+30,-150)
    up()
hideturtle()
done()
try:
    bye()
except Terminator:
    pass
