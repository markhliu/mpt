import requests
from bs4 import BeautifulSoup as bs
from yahoo_fin import stock_info as si

from mptpkg import print_say

# Define stock_price() function
def stock_price(v_inp):
    # Extract company name
    pos=v_inp.find("stock price of")
    myfirm=v_inp[pos+len("stock price of "):]
    # Extract the source code from the website
    res = requests.get('https://www.marketwatch.com/tools/quotes/lookup.asp?siteID=mktw&Lookup='+myfirm+'&Country=us&Type=All')
    # Prevent crashing in case there is no result
    try:
        res.raise_for_status()
        # Parse the code
        soup = bs(res.text, 'html.parser')
        # Collect all td tags from the source code
        tags = soup('td')
        # The text of the very first td tag is your ticker
        ticker = tags[0].text
        # Obtain real-time stock price from Yahoo
        price = round(float(si.get_live_price(ticker)),2)
        # Speak the stock price
        print_say(f"the stock price for {myfirm} is ${price}")
        # If price is not found, the script will tell you
    except:
        print_say("sorry, I cannot find what you are looking for!")

# Define stock_market() function
def stock_market():
        # Obtain real-time index values from Yahoo
        dow = round(float(si.get_live_price('^DJI')),2)
        sp500 = round(float(si.get_live_price('^GSPC')),2)
        # Announces the index values
        print_say(f"The Dow Jones Industry Average is {dow}.")
        print_say(f"The S&P 500 is {sp500}.")
