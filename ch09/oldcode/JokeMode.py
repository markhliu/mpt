# import needed modules
import random

# make sure you put mySAY.py and jokes.txt in the same folder as this program
from mySAY import printAndSAY

# define the Joke() function
def Joke():
    #read the content from the file jokes.txt
    with open('jokes.txt','r') as f:content=f.read()   
    #split the content at double line breaks
    jokelist=content.split('\n\n')
    #randomly selects a joke from the list
    joke=random.choice(jokelist)
    printAndSAY(joke)
