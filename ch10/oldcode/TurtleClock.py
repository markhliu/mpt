# import needed modules
from turtle import *
import time
import arrow

#set up the screen    
setup(800,600, 10, 70)
tracer(False)
bgcolor('lightgreen')
hideturtle()
# put the program in an infinite loop
while True:
    # clear the screen
    clear()
    # obtain the current time
    CurrentTime = arrow.utcnow().format('hh:mm:ss A')
    color('blue')
    up()
    goto(-300,50)
    # write the first line of text
    write('The Current Time Is\n',font=('Arial',50,'normal'))
    color('red')
    goto(-300,-100)
    # write what time it is
    write(CurrentTime,font=('Arial',80,'normal'))
    time.sleep(1)
    #put everything on screen
    update()
done()
try:
    bye()
except Terminator:
    pass
