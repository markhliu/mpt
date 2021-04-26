import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import matplotlib.dates as mdates
import requests

from datetime import date, timedelta 

from mptpkg import print_say

def price_plot(firm):
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
        end_date = date.today().strftime("%Y-%m-%d")
        start_date = (date.today() - timedelta(days = 180)).strftime("%Y-%m-%d")
        # Get stock price
        stock = pdr.get_data_yahoo(ticker, start = start_date, end = end_date)
        # Obtain dates
        stock['Date'] = stock.index.map(mdates.date2num)
        # Choose figure size
        fig = plt.figure(dpi = 128, figsize = (10, 6))
        # Format date to place on the x-axis
        formatter = mdates.DateFormatter('%m/%d/%Y')
        plt.gca().xaxis.set_major_formatter(formatter)
        # Plot data.
        plt.plot(stock['Date'], stock['Adj Close'], c = 'blue')
        # Format plot.
        plt.title(f"The Stock Price of {firm}", fontsize = 16)
        plt.xlabel('Date', fontsize = 10)
        fig.autofmt_xdate()
        plt.ylabel("Price", fontsize = 10)
        plt.show()    
        # Let you know that the plot is ready via voice and print
        print_say(f"OK, here is the stock price plot for {firm}.")
    except:
        print_say("Sorry, not a valid entry!")

