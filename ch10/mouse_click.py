import turtle as t

# Set up the screen
t.setup(620,620,360,100)
t.title("How Mouse-Clicks Work in Turtle Graphics")
# Define a function get_xy() to print the x and y value of the point you click
def get_xy(x,y):
    print(f'(x, y) is ({x}, {y})') 
# Hide turtle so that you don't see the arrowhead        
t.hideturtle()
# Bind the mouse click to the get_xy() function
t.onscreenclick(get_xy)
t.listen()    
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')
