import requests
from yahoo_fin import stock_info as si

from mptpkg import print_say

# Define stock_price() function
def stock_price(v_inp):
    # Extract company name
    pos = v_inp.find("stock price of")
    myfirm = v_inp[pos+len("stock price of "):]
    # Prevent crashing in case there is no result
    try:
        # Extract the source code from the website
        url = 'https://query1.finance.yahoo.com/v1/finance/search?q='+myfirm
        response = requests.get(url)
        # Read the JSON data
        response_json = response.json()
        # Obtain the value corresponding to "quotes"
        quotes = response_json['quotes']
        # Get the ticker symbol
        ticker = quotes[0]['symbol']
        # Obtain real-time stock price from Yahoo
        price = round(float(si.get_live_price(ticker)),2)
        # Speak the stock price
        print_say(f"the stock price for {myfirm} is {price} dollars")
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
