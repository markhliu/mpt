from turtle import *

Screen()
setup(600,500,100,200)
title('Python Turtle Graphics')
hideturtle()
up()
goto(150,100)
dot(120,'red')
goto(-150,100)
dot(135,'yellow')
goto(150,-100)
dot(125,'blue')
goto(-150,-100)
dot(140,'green')
done()
try:
    bye()
except Terminator:
    pass
