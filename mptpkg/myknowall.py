import wolframalpha
import wikipedia

from mptpkg import print_say

# Put your WolframApha APIkey below
APIkey = "{your APIkey}"
wolf = wolframalpha.Client(APIkey)

def know_all(v_inp):
    # Use try and except to prevent crashing
    try:
        # Look for answer in Wolfram Alpha
        res = wolf.query(v_inp)
        # Create a string variable ans to contain answers
        print_say(next(res.results).text)
    except:
        try:
            ans = wikipedia.summary(v_inp)
            print_say(ans[0:200])
        except:
            # If still no answer
            print_say('I am still learning. I don\'t know the answer to your question yet.')
            
        
