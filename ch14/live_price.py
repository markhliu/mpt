from yahoo_fin import stock_info as si

# Start an infinite loop
while True:
    # Obtain ticker symbol from you
    ticker = input("What's the ticker symbol of the stock you are looking for?\n")
    # If you want to stop, type in "done"
    if ticker == "done":
        break
    # Otherwise, type in a stock ticker symbol
    else:
        # Obtain live stock price from Yahoo
        price = si.get_live_price(ticker)
        # Print out the stock price
        print(f"The stock price for {ticker} is {price}.")

