# import the wolframalpha module
import wolframalpha

# enter your own WolframAlpha APIkey below
APIkey = "{your WolframAlpha APIkey}" 
wolf = wolframalpha.Client(APIkey)
# enter your query 
inp=input("What do you want to know from WolframAlpha?\n")
# send your query to WolframAlpha and get a response
response = wolf.query(inp)
# retrieve the text from the response
res = next(response.results).text 
# print out the response
print(res) 
