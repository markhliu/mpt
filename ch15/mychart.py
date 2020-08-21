import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc
import requests
from bs4 import BeautifulSoup as bs

from mptpkg import print_say

from datetime import date, timedelta

def candle_stick(firm):
    # Change the empty space to "+" 
    myfirm=firm.replace(' ', '+')
    # Extract the source code from the website
    res = requests.get('https://www.marketwatch.com/tools/quotes/lookup.asp?siteID=mktw&Lookup='+myfirm+'&Country=us&Type=All')
    try:
        res.raise_for_status()   
        # Parse the code
        soup = bs(res.text, 'html.parser')
        # Collect all td tags from the source code
        tags = soup('td')
        # The very first td tag is your ticker
        ticker = tags[0].text        
        # Set the start and end date
        start_date = (date.today() - timedelta(days=14)).strftime("%Y-%m-%d")
        end_date = date.today().strftime("%Y-%m-%d")
        # Get stock price
        stock = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
        # Obtain dates
        stock['Date']=stock.index.map(mdates.date2num)       
        # Choose the four daily prices: open, hihg, low, and close
        df_ohlc = stock[['Date','Open', 'High', 'Low', 'Close']]
        # Choose figure size
        figure, fig = plt.subplots(dpi=128, figsize = (8,4))
        # Format date
        formatter = mdates.DateFormatter('%m/%d/%Y')
        # Choose x-axis
        fig.xaxis.set_major_formatter(formatter)
        fig.xaxis_date()
        plt.setp(fig.get_xticklabels(), rotation = 10)
        # Create teh candlestick chart
        candlestick_ohlc(fig, 
                         df_ohlc.values, 
                         width=0.8, 
                         colorup='black', 
                         colordown='gray')
        # Put text in the chart that black means close is higher than open
        plt.figtext(0.3,0.2,'Black: Close > Open')
        # Put text in the chart that gray means close is lower than open
        plt.figtext(0.3,0.15,'Gray: Close < Open')
        # Put chart title and axis labels
        plt.title(f'Candlestick Chart for the Stock of {firm}')
        plt.ylabel('Pirce')
        plt.xlabel('Date')
        plt.show()
        print_say(f"Here is the candlestick chart for {firm}.") 
    except:
        print_say("Sorry, not a valid entry!")
        
        

