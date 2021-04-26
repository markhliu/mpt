from datetime import date, timedelta

import statsmodels.api as sm
from pandas_datareader import data as pdr
import requests

from mptpkg import voice_to_text, print_say

def alpha_beta(firm):
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
        # Set the start and end dates
        end_date = date.today().strftime("%Y-%m-%d")
        start_date = (date.today() - timedelta(days=180)).strftime("%Y-%m-%d")
        # Retieve prices
        sp = pdr.get_data_yahoo( "^GSPC", start = start_date, end = end_date)
        stock = pdr.get_data_yahoo(ticker, start = start_date, end = end_date)
        # Calculate returns for sp500 and the stock
        sp['ret_sp'] = (sp['Adj Close']/sp['Adj Close'].shift(1))-1
        stock['ret_stock'] = (stock['Adj Close']/stock['Adj Close'].shift(1))-1
        # Merge the two datasets, keep only returns
        df = sp[['ret_sp']].merge(stock[['ret_stock']], left_index = True, right_index = True) 
        # Add risk free rate (assume constant for simplicity) 
        df['rf'] = 0.00001
        # We need a constant to run regressions
        df['const'] = 1 
        df['exret_stock'] = df.ret_stock - df.rf
        df['exret_sp'] = df.ret_sp - df.rf
        # Remove missing values
        df.dropna(inplace = True) 
        # Calculate the stock's alpha and Beta
        reg = sm.OLS(endog = df['exret_stock'], exog = df[['const', 'exret_sp']], missing = 'drop')
        results = reg.fit()
        alpha = round(results.params['const']*100,3)
        beta = round(results.params['exret_sp'],2)
        # Speak the values of alpha and beta
        print_say(f'The alpha of the stock of {firm} is {alpha} percent.')
        print_say(f'The beta of the stock of {firm} is {beta}.')
    except:
        print_say("Sorry, not a valid entry!")

# Start an infinite loop
while True:
    # Obtain voice input from you
    print_say("How may I help you?")
    inp = voice_to_text()
    print_say(f"You said {inp}.")
    # If you want to stop, say "stop listening"
    if inp == "stop listening":
        print_say("Nice talking to you, goodbye!")
        break
    # If keywords in command, go to the stock report mode
    elif "stock report for" in inp:
        # Locate the company name 
        pos = inp.find('stock report for ')
        firm = inp[pos+len('stock report for '):]
        alpha_beta(firm)
        continue
    # Otherwise, go to the next iteration
    else:
        continue
    


