import wolframalpha
import wikipedia

# You must put your WolframApha APIkey below
APIkey = "{your WolframAlpha appID here}" 
wolf = wolframalpha.Client(APIkey)

while True:
    # Put your question here 
    inp=input("What do you want to know?\n")
    # Stop the loop if you type in "done"
    if inp=="done":
        break
    # Use try and except to prevent crashing
    try:
        # Look for answer in Wolfram Alpha
        res = wolf.query(inp)
        # Create a string variable ans to contain answers
        ans=''
        print(next(res.results).text)
        ans += str(next(res.results).text)
    except:
        pass
    # If the answer string is empty, try Wikipedia
    if len(ans)==0:
        try:
            ans=wikipedia.summary(inp)
        except:
            pass
        print(ans[0:200])
        # If the answer string is still empty, no answer
        if len(ans)==0:
            print('I am still learning. I don\'t know the answer to your question yet.')
