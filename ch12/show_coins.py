import turtle as t
from tkinter import PhotoImage
from time import sleep

# Set up the board
t.setup(600,500)
t.hideturtle()
t.tracer(False)
t.bgcolor("lavender")
t.title("Guess the Word Game in Turtle Graphics")
# Define a variable to count how many guesses left
score = 6
# Create a second turtle to show guesses left
left = t.Turtle()
left.up()
left.hideturtle()
left.goto(-290,200)
left.write(f"guesses left:   {score}", font = ('Arial',20,'normal'))
# Put incorrect guesses on top
t.up()
t.goto(-290,150)
t.write("incorrect guesses:", font = ('Arial',20,'normal'))
# Put four empty spaces for the four letters at bottom
for x in range(4):
    t.goto(-275+150*x,-200)
    t.down()
    t.goto(-175+150*x,-200)   
    t.up()
# Load a picture of the coin to the script
coin = PhotoImage(file = "cash.png").subsample(10,10)
t.addshape("coin", t.Shape("image", coin))
# Create six coin on screen 
coins = [0]*6
for i in range(6):
    coins[i] = t.Turtle('coin')
    coins[i].up()
    coins[i].goto(-100 + 50 *i, -10)
t.update()
sleep(3)
# Make the coins disappear one at a time
for i in range(6):
    coins[i].hideturtle()
    t.update()
    sleep(1)
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')
