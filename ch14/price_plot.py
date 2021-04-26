import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import matplotlib.dates as mdates

# Set the start and end dates
start_date = "2019-12-01"
end_date = "2020-05-31"

# Choose stock ticker symbol
ticker = "TSLA"
# Get stock price
stock = pdr.get_data_yahoo(ticker, start = start_date, end = end_date)
print(stock)
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
plt.title("The Stock Price of Tesla", fontsize = 16)
plt.xlabel('Date', fontsize = 10)
fig.autofmt_xdate()
plt.ylabel("Price", fontsize = 10)
plt.show()
