import requests

# Specify the url to find the bitcoin price
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
# Retrieve the live information from bitcoin url
response = requests.get(url)
# Read the JSON data
response_json = response.json()
# Obtain the USD dictionary
usd = response_json['bpi']['USD']
# Get the price
price = usd['rate_float']
print(f"The Bitcoin price is {price} dollars.")
