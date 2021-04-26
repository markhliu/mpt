#import needed modules
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

#set the start and end date
start_date = "2020-05-01"
end_date = "2020-05-31"
#choose stock ticker symbol
ticker = "AMZN"
#get stock price
stock = pdr.get_data_yahoo(ticker, start = start_date, end = end_date)
#obtain dates
stock['Date'] = stock.index.map(mdates.date2num)
#choose the four daily prices: open, hihg, low, and close
df_ohlc = stock[['Date','Open', 'High', 'Low', 'Close']]
#choose figure size
figure, fig = plt.subplots(dpi = 128, figsize = (8,4))
#format date
formatter = mdates.DateFormatter('%m/%d/%Y')
#choose x-axis
fig.xaxis.set_major_formatter(formatter)
fig.xaxis_date()
plt.setp(fig.get_xticklabels(), rotation = 10)
#create teh candlestick chart
candlestick_ohlc(fig, 
                 df_ohlc.values, 
                 width = 0.8, 
                 colorup = 'black', 
                 colordown = 'gray')
#put text in the chart 
plt.figtext(0.3,0.2,'Black: Close > Open')
#put text in the chart that red color means close is lower than open
plt.figtext(0.3,0.15,'Gray: Close < Open')
#put chart title and axis labels
plt.title(f'Candlesticks Chart for {ticker} in May 2020')
plt.ylabel('Pirce')
plt.xlabel('Date')
plt.show()
