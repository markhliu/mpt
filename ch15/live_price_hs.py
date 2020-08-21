import requests
from bs4 import BeautifulSoup as bs
from yahoo_fin import stock_info as si

from mptpkg import voice_to_text, print_say

# Start an infinite loop
while True:
    # Obtain company name from you
    print_say("Which company's stock price do you want to know?")
    firm=voice_to_text()
    print_say(f"You just said {firm}.")
    # If you want to stop, type in "stop listening"
    if firm =="stop listening":
        print_say("OK, goodbye then!")
        break
    # Otherwise, say a company name
    else:
        # Change the empty space to "+" 
        myfirm=firm.replace(' ', '+')
        # Extract the source code from the website
        res = requests.get('https://www.marketwatch.com/tools/quotes/lookup.asp?siteID=mktw&Lookup='+myfirm+'&Country=us&Type=All')
        # Prevent crashing in case there is no result
        try:
            res.raise_for_status()   
            # Parse the code
            soup = bs(res.text, 'html.parser')
            # Collect all td tags from the source code
            tags = soup('td')
            # The very first td tag is your ticker
            ticker = tags[0].text
            # Obtain live stock price from Yahoo
            price = round(float(si.get_live_price(ticker)),2)
            # Speak the stock price
            print_say(f"The stock price for {firm} is {price}.")        
        # In case the price cannot be found, the program will tell you
        except:
            print_say("Sorry, I cannot find what you are looking for!")        
        continue


