# Import the wolframalpha module
import wolframalpha

# Enter your own WolframAlpha APIkey below
APIkey = "{your WolframAlpha APIkey}" 
wolf = wolframalpha.Client(APIkey)
# Enter your query 
inp = input("What do you want to know from WolframAlpha?\n")
# Send your query to WolframAlpha and get a response
response = wolf.query(inp)
# Retrieve the text from the response
res = next(response.results).text 
# Print out the response
print(res) 
