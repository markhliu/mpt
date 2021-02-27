import turtle as t
from random import choice

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
t.update()
# Put words in a dictionary and randomly pick one
words = ['that', 'with', 'have', 'this', 'will', 'your', 
   'from', 'they', 'know', 'want', 'been', 
   'good', 'much', 'some', 'time']
word = choice(words)
# Create a missed list
missed = []
# Start the game loop
while True:
    # Take written input 
    inp = input("What's your guess?\n").lower()
    # Stop the loop if you key in "done"
    if inp == "done":
        break
    # Check if the letter is in the word
    elif inp in list(word):
        # If yes, put it in the right position(s)
        for w in range(4):
            if inp == list(word)[w]:
                t.goto(-250+150*w,-190)
                t.write(inp, font = ('Arial',60,'normal'))
    # If the letter is not in the word, show it at the top
    else:
        missed.append(inp)
        t.goto(-290+80*len(missed),60)
        t.write(inp, font = ('Arial',60,'normal'))
    # Update everything that happens in the iteration
    t.update()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')
