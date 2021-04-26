import requests

# Start an infinite loop
while True:
    # Obtain company name from you
    firm = input("Which company's ticker are you looking for?\n")
    # If you want to stop, type in "done"
    if firm == "done":
        break
    # Otherwise, type in a company name
    else:
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
            # Print out the ticker
            print(f"The ticker symbol for {firm} is {ticker}.")
        except:
            print("Sorry, not a valid entry!")
        continue

