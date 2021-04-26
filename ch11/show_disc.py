import turtle as t

# Set up the screen
t.setup(700,600,10,70)
t.hideturtle()
t.tracer(False)
t.bgcolor("lightgreen")
t.title("Connect Four in Turtle Graphics")
# Draw six thick vertical lines
t.pensize(5)
for i in range(-250,350,100):  
    t.up()
    t.goto(i,-350)
    t.down()
    t.goto(i,350)
    t.up()
# Draw five thin gray horizontal lines to form grid    
t.pensize(1)
t.pencolor("grey")
for i in range(-200,300,100):  
    t.up()
    t.goto(-350,i)
    t.down()
    t.goto(350,i)
    t.up()
# Write column numbers on the board
colnum = 1
for x in range(-300, 350, 100):
    t.goto(x,270)
    t.write(colnum,font = ('Arial',20,'normal'))
    colnum += 1
# The red player moves first
turn = "red"
# The x coordinates of the center of the 7 columns
xs = [-300,-200,-100,0,100,200,300]
# The y coordinates of the center of the 6 rows
ys = [-250,-150,-50,50,150,250]
# Keep track of the occupied cells
occupied = [list(),list(),list(),list(),list(),list(),list()]
# Define a function conn() to place a disc in a cell
def conn(x,y):
    # Make the variable turn a globale variable
    global turn
    # Calculate the column number based on x and y values
    if -350<x<350 and -300<y<300:
        col = int((x+450)//100)
    else:
        print('You have clicked outside the game board!')
    # Calculate the lowest available row number in that column
    row = len(occupied[col-1])+1
    # Go to the cell and place a dot of the player's color
    t.up()
    t.goto(xs[col-1],ys[row-1])
    t.dot(80,turn)
    # Add the move to the occupied list to keep track
    occupied[col-1].append(turn)
    # Give the turn to the other player
    if turn == "red":
        turn = "yellow"
    else:
        turn = "red"     
# Bind the mouse click to the conn() function
t.onscreenclick(conn)
t.listen()    
t.done()        
try:
    t.bye()
except t.Terminator:
    print('exit turtle')

