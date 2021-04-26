import tkinter as tk
import requests

import arrow

from mptpkg import print_say

# Specify the url to find the bitcoin price
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
# Create a root window hold all widgets
root = tk.Tk()
# Specify the title and size of the root window
root.title("Bitcoin Watch")
root.geometry("1000x400")
# Create a first label using hte Label() function
label = tk.Label(text="", fg="Blue", font=("Helvetica", 80))
label.pack()
# Create a second label
label2 = tk.Label(text="", fg="Red", font=("Helvetica", 60))
label2.pack()
# Set up the price bounds
response = requests.get(url)
response_json = response.json()
oldprice = response_json['bpi']['USD']['rate_float']
maxprice = oldprice * 1.05
minprice = oldprice * 0.95
print_say(f'The Bitcoin price is now {oldprice}!')


# Define the bitcoin_watch() function
def bitcoin_watch():
    global oldprice
    # Get the live information from bitcoin url
    response = requests.get(url)
    response_json = response.json()
    price = response_json['bpi']['USD']['rate_float']
    # If there is update in price, announce it    
    if price != oldprice:
        oldprice = price
        print_say(f'The Bitcoin price is now {oldprice}!')
    # If price goes out of bounds, announce it    
    if price > maxprice:
        print_say('The Bitcoin price has gone above the upper bound!')
    if price < price:
        print_say('The Bitcoin price has gone below the lower bound!')
        # Obtain current date and time information         
    tdate = arrow.utcnow().format('MMMM DD, YYYY')
    tm = arrow.utcnow().format('hh:mm:ss A')
    # Put the date and time information in the first label         
    label.configure(text=tdate + "\n" + tm)
    # Put all the five messages on the stock market in the second label        
    label2.configure(text=f'Bitcoin: {price}', justify=tk.LEFT)
    # call the bitcoin_watch() function after 1000 milliseconds
    root.after(1000, bitcoin_watch)


# call the bitcoin_watch() function
bitcoin_watch()
# run the game loop
root.mainloop()



