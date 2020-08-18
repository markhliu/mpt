from turtle import *

#set up the screen  
Screen()  
setup(810,710, 10, 70)
hideturtle()
tracer(False)
bgcolor('lightgreen')
#draw the vertical lines to create 7 columns
pensize(5)
for i in range(-350,400,100):  
    up()
    goto(i, -298)
    down()
    goto(i, 303)
    up()
#draw the horizontal lines to separate the screen in 6 rows    
pensize(1)
color('gray')
for i in range(-300,400,101):  
    up()
    goto(-350,i)
    down()
    goto(350,i)
    up()   
done()
try:
    bye()
except Terminator:
    pass