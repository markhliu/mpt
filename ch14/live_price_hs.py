import requests
from yahoo_fin import stock_info as si

from mptpkg import voice_to_text, print_say

# Start an infinite loop
while True:
    # Obtain company name from you
    print_say("Which company's stock price do you want to know?")
    firm = voice_to_text()
    print_say(f"You just said {firm}.")
    # If you want to stop, type in "stop listening"
    if firm == "stop listening":
        print_say("OK, goodbye then!")
        break
    # Otherwise, say a company name
    else:
        try:
            # Extract the source code from the website
            url = 'https://query1.finance.yahoo.com/v1/finance/search?q='+firm
            response = requests.get(url)
            # Read the JSON data
            response_json = response.json()
            # Obtain the value corresponding to "quotes"
            quotes = response_json['quotes']
            # Get the ticker symbol
            ticker = quotes[0]['symbol']

            # Obtain live stock price from Yahoo
            price = round(float(si.get_live_price(ticker)),2)
            # Speak the stock price
            print_say(f"The stock price for {firm} is {price}.")        
        # In case the price cannot be found, the program will tell you
        except:
            print_say("Sorry, I cannot find what you are looking for!")        
        continue


