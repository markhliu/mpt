import turtle as t
import time

import arrow

# Set up the screent.
t.setup(800,600, 10, 70)
t.tracer(False)
t.bgcolor('lightgreen')
t.hideturtle()
# Put the program in an infinite loop
while True:
    # Clear the screen
    t.clear()
    # Obtain the current time
    current_time = arrow.utcnow().format('hh:mm:ss A')
    t.color('blue')
    t.up()
    t.goto(-300,50)
    # Write the first line of text
    t.write('The Current Time Is\n',font=('Arial',50,'normal'))
    t.color('red')
    t.goto(-300,-100)
    # Write what time it is
    t.write(current_time,font=('Arial',80,'normal'))
    time.sleep(1)
    # Put everything on screen
    t.update()
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')

