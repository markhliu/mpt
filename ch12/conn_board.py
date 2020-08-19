from turtle import *

Screen()
setup(700, 600, 10, 70)
hideturtle()
tracer(False)
bgcolor("lightgreen")
title("Connect Four in Turtle Graphics")
# Draw six thick vertical lines
pensize(5)
for i in range(-250,350,100):  
    up()
    goto(i, -350)
    down()
    goto(i, 350)
    up()
# Draw five thin gray horizontal lines to form grid    
pensize(1)
pencolor("grey")
for i in range(-200,300,100):  
    up()
    goto(-350,i)
    down()
    goto(350,i)
    up()
# Write column numbers on the board
colnum=1
for x in range(-300, 350, 100):
    goto(x,270)
    write(colnum,font=('Arial',20,'normal'))
    colnum += 1
done()
try:
    bye()
except Terminator:
    pass
