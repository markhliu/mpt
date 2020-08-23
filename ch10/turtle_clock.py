from turtle import *
import time
import arrow

# Set up the screen    
setup(800,600, 10, 70)
tracer(False)
bgcolor('lightgreen')
hideturtle()
# Put the program in an infinite loop
while True:
    # Clear the screen
    clear()
    # Obtain the current time
    current_time = arrow.utcnow()
    local = current_time.to('US/Pacific').format('hh:mm:ss A')
    color('blue')
    up()
    goto(-300,50)
    # Write the first line of text
    write('The Current Time Is\n',font=('Arial',50,'normal'))
    color('red')
    goto(-300,-100)
    # Write what time it is
    write(local,font=('Arial',80,'normal'))
    time.sleep(1)
    # Put everything on screen
    update()
done()
try:
    bye()
except Terminator:
    pass
