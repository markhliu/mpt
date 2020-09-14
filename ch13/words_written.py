import turtle as t
from random import choice
from tkinter import messagebox, PhotoImage

# Set up the board
t.setup(600,500)
t.hideturtle()
t.tracer(False)
t.bgcolor("azure")
t.title("Words Game in Turtle Graphics")
# Put incorrect guesses on top
t.up()
t.goto(-290,150)
t.write("incorrect guesses:",font=('Arial',20,'normal'))
# Put four empty spaces for the 4 letters at bottom
for x in range(4):
    t.goto(-275+150*x,-200)
    t.down()
    t.goto(-175+150*x,-200)   
    t.up()
# Put the most common 4-letter words in a dictionary
words=['that', 'with', 'have', 'this', 'will', 'your', 
   'from', 'they', 'know', 'want', 'been', 
   'good', 'much', 'some', 'time']
# Randomly pick one word
word=choice(words)
# Create a missed list
missed=[]
# Define a variable to count how many chances left
score=6
# Create a second turtle to show chances left
left=t.Turtle()
left.up()
left.hideturtle()
left.goto(-290,200)
left.write(f"chances left:   {score}",font=('Arial',20,'normal'))
# Draw coins on screen
coin = PhotoImage(file="cash.png").subsample(10,10)
t.addshape("c", t.Shape("image", coin))
coins=[t.Turtle('c'),t.Turtle('c'),t.Turtle('c'),t.Turtle('c'),t.Turtle('c'),t.Turtle('c')]
for i, coin in enumerate(coins):
    coin.up()
    coin.goto(-100+50*i,0)
t.update()
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
        # Check if the picked letter is in the word
        if inp in list(word):
            # If yes, put it in the right position(s)
            for w in range(4):
                if inp==list(word)[w]:
                    t.goto(-250+150*w,-190)
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
            # Remove a coin
            coins[-(6-score)].hideturtle()
            t.update()
            # Update the number of chances left on board
            left.clear()
            left.write(f"chances left:   {score}",font=('Arial',20,'normal'))
            t.update()            
            missed.append(inp)
            t.goto(-290+80*len(missed),50)
            t.write(inp,font=('Arial',60,'normal'))
            if len(missed)==6:
                # If all six chances are used up, end game
                messagebox.showinfo("End Game","Sorry, you used up all your six chances!")
                break 
        # Remove the picked letter from the validinputs list
        validinputs.remove(inp)
    # Update everything happens in the iteration
    t.update()
try:
    t.bye()
except t.Terminator:
    pass

