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
# The blue player moves first
turn = "blue"
# Define a function mark_cell() to place a dot in the cell
def mark_cell(x,y):
    # Make the variable turn a globale variable
    global turn
    # Calculate the cell number based on x and y values
    if -300<x<300 and -300<y<300:
        col = int((x+500)//200)
        row = int((y+500)//200)
        # The cell number is a string varibale
        cellnumber = str(col+(row-1)*3)
    else:
        print('you have clicked outside the game board')
    # Go to the corresponding cell and place a dot of the player's color
    t.up()
    t.goto(cellcenter[cellnumber])
    t.dot(180,turn)
    t.update()
    # Give the turn to the other player
    if turn == "blue":
        turn = "white"
    else:
        turn = "blue"       
# Hide turtle so that you don't see the arrowhead        
t.hideturtle()
# Bind the mouse click to the CellNumber() function
t.onscreenclick(mark_cell)
t.listen()    
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')
