import wolframalpha
import wikipedia

# Add the one-level-up directory to the search space
import sys
sys.path.append('../')
from mypkg.mysay import print_say

# Put your WolframApha APIkey below
APIkey = {your APIkey} 
wolf = wolframalpha.Client(APIkey)

def know_all(v_inp):
    # Use try and except to prevent crashing
    try:
        # Look for answer in Wolfram Alpha
        res = wolf.query(v_inp)
        # Create a string variable ans to contain answers
        ans=''
        print_say(next(res.results).text)
        ans += str(next(res.results).text)
    except:
        pass
    # If the answer string is empty, try Wikipedia
    if len(ans)==0:
        try:
            ans=wikipedia.summary(v_inp)
        except:
            pass
        print_say(ans[0:200])
        # if the answer string is still empty, no answer
        if len(ans)==0:
            print_say('I am still learning. I don\'t know the answer to your question yet.')
            
        
