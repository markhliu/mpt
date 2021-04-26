import turtle as t

# Set up the screen
t.setup(600,600,10,70)
t.tracer(False)
t.bgcolor("red")
t.title("Tic-Tac-Toe in Turtle Graphics")
# Draw horizontal lines and vertical lines to form grid
t.pensize(5)
for i in (-100,100):  
    t.up()
    t.goto(i,-300)
    t.down()
    t.goto(i,300)
    t.up()
    t.goto(-300,i)
    t.down()
    t.goto(300,i)
    t.up()
# Create a dictionary to map cell numbers to the center coordinates
cellcenter = {'1':(-200,-200), '2':(0,-200), '3':(200,-200),
            '4':(-200,0), '5':(0,0), '6':(200,0),
            '7':(-200,200), '8':(0,200), '9':(200,200)} 
# Go to the center of each cell, write down the cell number
for cell, center in list(cellcenter.items()):
    t.goto(center)
    t.write(cell,font = ('Arial',20,'normal'))
# Define a function cell_number() to print out the cell number
def cell_number(x,y):
    if -300<x<300 and -300<y<300:
        # Calculate the column number based on x value
        col = int((x+500)//200)
        print('column number is ', col)
        # Calculate the row number based on y value
        row = int((y+500)//200)
        print('row number is ', row)
        # Calculate the cell number based on col and row
        cell_number = col + (row - 1)*3
        print('cell number is ', cell_number)
    else:
        print('you have clicked outside the game board')
# Hide turtle so that you don't see the arrowhead        
t.hideturtle()
# Bind the mouse click to the cell_number() function
t.onscreenclick(cell_number)
t.listen()    
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')
