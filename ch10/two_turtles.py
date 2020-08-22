from turtle import *

# Set up the screen    
setup(810,710, 10, 70)
tracer(False)
hideturtle()
bgcolor('lightgreen')
color('blue')
pensize(5)
up()
goto(-200,-100)
down()
forward(400)
left(90)
forward(400)
left(90)
forward(400)
left(90)
forward(400)
# Create a second turtle 
msg = Turtle()
msg.hideturtle()
msg.up()
msg.color('red')
msg.goto(-300,-200)
msg.write('this is written by the second turtle',font=('Arial',30,'normal'))
update()
done()
try:
    bye()
except Terminator:
    pass



