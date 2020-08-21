import requests
from bs4 import BeautifulSoup as bs

# Start an infinite loop
while True:
    # Obtain ticker symbol from you
    firm=input("Which company's ticker are you looking for?\n")
    # If you want to stop, type in "done"
    if firm =="done":
        break
    # Otherwise, type in a company name
    else:
        # Change the empty space to "+" 
        myfirm=firm.replace(' ', '+')
        # Extract the source code from the website
        res = requests.get('https://www.marketwatch.com/tools/quotes/lookup.asp?siteID=mktw&Lookup='+myfirm+'&Country=us&Type=All')
        try:
            res.raise_for_status()   
        except:
            print("sorry, not a valid entry")
            continue
        # Parse the code
        soup = bs(res.text, 'html.parser')
        # Collect all td tags from the source code
        tags = soup('td')
        # The very first td tag is your ticker
        ticker = tags[0].text
        # Print out the ticker
        print(f"The ticker symbol for {firm} is {ticker}.")


