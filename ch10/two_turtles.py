from turtle import *

# Set up the screen    
setup(810,710, 10, 70)
tracer(False)
hideturtle()
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
msg.goto(0,-200)
msg.write(
  'Written by the second turtle',
  align="center",
  font=('Arial',30,'normal'))
update()

# Trick to close the window by clicking anywhere on the Screen
screen = Screen()
screen.exitonclick()

done()
try:
    bye()
except Terminator:
    pass


