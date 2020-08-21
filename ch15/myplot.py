import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import matplotlib.dates as mdates
import requests
from bs4 import BeautifulSoup as bs

from datetime import date, timedelta 

from mptpkg import print_say

def price_plot(firm):
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
        end_date = date.today().strftime("%Y-%m-%d")
        start_date = (date.today() - timedelta(days=180)).strftime("%Y-%m-%d")
        # Get stock price
        stock = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
        # Obtain dates
        stock['Date']=stock.index.map(mdates.date2num)
        # Choose figure size
        fig = plt.figure(dpi=128, figsize=(10, 6))
        # Format date to place on the x-axis
        formatter = mdates.DateFormatter('%m/%d/%Y')
        plt.gca().xaxis.set_major_formatter(formatter)
        # Plot data.
        plt.plot(stock['Date'], stock['Adj Close'], c='blue')
        # Format plot.
        plt.title(f"The Stock Price of {firm}", fontsize=16)
        plt.xlabel('Date', fontsize=10)
        fig.autofmt_xdate()
        plt.ylabel("Price", fontsize=10)
        plt.show()    
        # Let you know that the plot is ready via voice and print
        print_say(f"OK, here is the stock price plot for {firm}.")
    except:
        print_say("Sorry, not a valid entry!")

