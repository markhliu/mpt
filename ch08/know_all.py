import wolframalpha
import wikipedia

# You must put your WolframApha APIkey below
APIkey = "{your WolframAlpha appID here}" 
wolf = wolframalpha.Client(APIkey)

while True:
    # Put your question here 
    inp = input("What do you want to know?\n")
    # Stop the loop if you type in "done"
    if inp == "done":
        break
    # Use try and except to prevent crashing
    try:
        # Look for answer in Wolfram Alpha
        res = wolf.query(inp)
        # Create a string variable ans to contain answers
        print(next(res.results).text)
    except:
        try:
            ans = wikipedia.summary(inp)
            print(ans)
        except:
            print('I am still learning. I don\'t know the answer to your question yet.')
