import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
import requests

from mptpkg import print_say

from datetime import date, timedelta

def candle_stick(firm):
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
        # Set the start and end date
        start_date = (date.today() - timedelta(days = 14)).strftime("%Y-%m-%d")
        end_date = date.today().strftime("%Y-%m-%d")
        # Get stock price
        stock = pdr.get_data_yahoo(ticker, start = start_date, end = end_date)
        # Obtain dates
        stock['Date'] = stock.index.map(mdates.date2num)       
        # Choose the four daily prices: open, hihg, low, and close
        df_ohlc = stock[['Date','Open', 'High', 'Low', 'Close']]
        # Choose figure size
        figure, fig = plt.subplots(dpi = 128, figsize = (8,4))
        # Format date
        formatter = mdates.DateFormatter('%m/%d/%Y')
        # Choose x-axis
        fig.xaxis.set_major_formatter(formatter)
        fig.xaxis_date()
        plt.setp(fig.get_xticklabels(), rotation = 10)
        # Create teh candlestick chart
        candlestick_ohlc(fig, 
                         df_ohlc.values, 
                         width = 0.8, 
                         colorup = 'black', 
                         colordown = 'gray')
        # Put text in the chart that black means close is higher than open
        plt.figtext(0.3,0.2,'Black: Close > Open')
        # Put text in the chart that gray means close is lower than open
        plt.figtext(0.3,0.15,'Gray: Close < Open')
        # Put chart title and axis labels
        plt.title(f'Candlestick Chart for the Stock of {firm}')
        plt.ylabel('Price')
        plt.xlabel('Date')
        plt.show()
        print_say(f"Here is the candlestick chart for {firm}.") 
    except:
        print_say("Sorry, not a valid entry!")
        
        
