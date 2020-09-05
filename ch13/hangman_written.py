import turtle as t
from random import choice
from tkinter import messagebox

# Set up the board
t.setup(600,900)
t.hideturtle()
t.tracer(False)
t.bgcolor("azure")
t.title("A Hangman Game in Turtle Graphics")
# Draw the gallows
t.pensize(5)
t.pencolor("black")
t.up()
t.goto(0,220)
t.down()
t.goto(0,260)
t.goto(250,260)
t.goto(250,-300)
# Put incorrect guesses on top
t.up()
t.goto(-290,350)
t.write("incorrect guesses:",font=('Arial',20,'normal'))
# Put four empty spaces for the 4 letters at bottom
t.goto(-275,-400)
t.down()
t.goto(-175,-400)   
t.up()
t.goto(-125,-400)
t.down()
t.goto(-25,-400)   
t.up()
t.goto(25,-400)
t.down()
t.goto(125,-400)   
t.up()
t.goto(175,-400)
t.down()
t.goto(275,-400)   
t.up()
# Put the most common 4-letter words in a dictionary and randomly pick one
words=['that', 'with', 'have', 'this', 'will', 'your', 
       'from', 'they', 'know', 'want', 'been', 
       'good', 'much', 'some', 'time']
word=choice(words)
# Create a missed list
missed=[]
# Define a variable to count how many chances left
score=6
# Create a second turtle to show chances left
left=t.Turtle()
left.up()
left.hideturtle()
left.goto(-290,400)
left.write(f"chances left:   {score}",font=('Arial',20,'normal'))
# Define the draw_head() function
def draw_head():
    t.up()
    t.goto(0,170)
    t.dot(120,"black")
# Define the draw_torso() function
def draw_torso():
    t.up()
    t.goto(0,100)
    t.down()
    t.goto(0,-100)
    t.up()
# Define the draw_left_arm() functiont.
def draw_left_arm():
    t.up()
    t.goto(0,100)
    t.down()
    t.goto(-100,-100)
    t.up()   
# Define the draw_right_arm() functiont.t.
def draw_right_arm():
    t.up()
    t.goto(0,100)
    t.down()
    t.goto(100,-100)
    t.up()   
# Define the draw_left_leg() functiont.t.
def draw_left_leg():
    t.up()
    t.goto(0,-100)
    t.down()
    t.goto(-100,-300)
    t.up()   
# Define the draw_right_leg() function 
def draw_right_leg():
    t.up()
    t.goto(0,-100)
    t.down()
    t.goto(100,-300)
    t.up()    
# Prepare the validinputs and gotright lists
validinputs=list('abcdefghijklmnopqrstuvwxyz')
gotright=[]
# Start the game loop
while True:
    # Take written input 
    inp=input("What's your choice?\n").lower()
    # Stop the loop if you key in "done"
    if inp=="done":
        break
    # If the letter is not a valid input, remind
    elif inp not in validinputs:
        messagebox.showerror("Error","Sorry, that's an invalid input!")
    # Otherwise, go ahead with the game
    else:  
        # Check if the picked letter is in the word, if yes, put it in the right position(s)
        if inp in list(word):
            if inp==list(word)[0]:
                t.goto(-250,-390)
                t.write(inp,font=('Arial',60,'normal'))
                gotright.append(inp)
            if inp==list(word)[1]:
                t.goto(-100,-390)
                t.write(inp,font=('Arial',60,'normal'))
                gotright.append(inp)
            if inp==list(word)[2]:
                t.goto(40,-390)
                t.write(inp,font=('Arial',60,'normal'))
                gotright.append(inp)
            if inp==list(word)[3]:
                t.goto(190,-390)
                t.write(inp,font=('Arial',60,'normal')) 
                gotright.append(inp)
            # If got four positions right, the player wins
            if len(gotright)==4:
                messagebox.showinfo("End Game","Great job, you got the word right!")
                break
        # If the picked letter is not in the word, show it at the top
        else:
            # Reduce chances left by 1
            score -= 1
            # Update the number of chances left on board
            left.clear()
            left.write(f"chances left:   {score}",font=('Arial',20,'normal'))
            t.update()            
            # Draw body part
            missed.append(inp)
            t.goto(-290+80*len(missed),260)
            t.write(inp,font=('Arial',60,'normal'))
            if len(missed)==1:
                draw_head()
            elif len(missed)==2:
                draw_torso()
            elif len(missed)==3:
                draw_left_arm()
            elif len(missed)==4:
                draw_right_arm()
            elif len(missed)==5:
                draw_left_leg()
            elif len(missed)==6:
                draw_right_leg()
                # If all six changes are used up, end game
                messagebox.showinfo("End Game","Sorry, you used up all your six chances!")
                break 
        # Remove the picked letter from the validinputs list
        validinputs.remove(inp)
    # Update everything happens in the iteration
    t.update()
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')
