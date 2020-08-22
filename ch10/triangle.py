from turtle import *

Screen()
setup(600,500,100,200)
bgcolor('springgreen3')
title('Python Turtle Graphics')
hideturtle()
tracer(False)
pencolor('blue')
pensize(5)
up()
goto(-50,-50)
down()
goto(50,-50)
goto(0,100)
goto(-50,-50)
update()
done()
try:
    bye()
except Terminator:
    pass