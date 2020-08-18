# import the needed modules
import wolframalpha
import wikipedia

# you must put your WolframApha APIkey below
APIkey = "{your WolframAlpha appID here}" 
wolf = wolframalpha.Client(APIkey)

while True:
    # Put your question here 
    inp=input("What do you want to know?\n")
    # stop the loop if you type in "done"
    if inp=="done":
        break
    #look for answer in Wolfram Alpha
    res = wolf.query(inp)
    # create a string variable ans to contain answers
    ans=''
    # use try and except to prevent crashing
    try:
        print(next(res.results).text)
        ans += str(next(res.results).text)
    except:pass
    # if the answer string is empty, try Wikipedia
    if len(ans)==0:
        try:
            ans=wikipedia.summary(inp)
        except:pass
        print(ans[0:200])
        # if the answer string is still empty, no answer
        if len(ans)==0:
            print('I am still learning. I don\'t know the answer to your question yet')
