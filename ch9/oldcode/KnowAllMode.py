#inport the needed modules
import wolframalpha
import wikipedia

# make sure you put mySAY.py in the same folder as this program
from mySAY import printAndSAY

# you must put your WolframApha APIkey below
APIkey = "your api here" 
wolf = wolframalpha.Client(APIkey)

def KnowAll(v_inp):
    #look for answer in Wolfram Alpha
    res = wolf.query(v_inp)
    # create a string variable ans to contain answers
    ans=''
    # use try and except to prevent crashing
    try:
        printAndSAY(next(res.results).text)
        ans += str(next(res.results).text)
    except:pass
    # if the answer string is empty, try Wikipedia
    if len(ans)==0:
        try:
            ans=wikipedia.summary(v_inp)
        except:pass
        printAndSAY(ans[0:200])
        # if the answer string is still empty, no answer
        if len(ans)==0:
            printAndSAY('I am still learning. I don\'t know the answer to your question yet')
            
        
