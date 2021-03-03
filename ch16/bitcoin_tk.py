import tkinter as tk
import requests
import time
from datetime import datetime
print(datetime.today().strftime("%B %d, %Y"))

# Specify the url to find the Bitcoin price
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
# Create a root window hold all widgets
root = tk.Tk()
# Specify the title and size of the root window
root.title("Bitcoin Watch")
root.geometry("1000x400")
# Create a first label using the Label() function
label = tk.Label(text="", fg="Blue", font=("Helvetica", 80))
label.pack()
# Create a second label
label2 = tk.Label(text="", fg="Red", font=("Helvetica", 60))
label2.pack()

# Define the bitcoin_watch() function
def bitcoin_watch():
    # Get the live information from Bitcoin url
    response = requests.get(url)
    response_json = response.json()
    price = response_json['bpi']['USD']['rate_float']
    # Obtain current date and time information         
    tdate = datetime.today().strftime("%B %d, %Y")
    tm = time.strftime("%H:%M:%S")
    # Put the date and time information in the first label         
    label.configure(text=tdate + "\n" + tm)
    # Put price info in the second label        
    label2.configure(text=f'Bitcoin: {price}', justify=tk.LEFT)
    # Call the bitcoin_watch() function after 1000 milliseconds
    root.after(1000, bitcoin_watch)

# Call the bitcoin_watch() function
bitcoin_watch()

# Run the game loop
root.mainloop()
