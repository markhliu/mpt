from datetime import date, timedelta

import statsmodels.api as sm
from pandas_datareader import data as pdr

# Set the start and end dates
end_date = date.today().strftime("%Y-%m-%d")
start_date = (date.today() - timedelta(days = 180)).strftime("%Y-%m-%d")
market = "^GSPC" 
ticker = "MSFT"
# Retieve prices
sp = pdr.get_data_yahoo(market, start = start_date, end = end_date)
stock = pdr.get_data_yahoo(ticker, start = start_date, end = end_date)
# Calculate returns for sp500 and the stock
sp['ret_sp'] = (sp['Adj Close']/sp['Adj Close'].shift(1))-1
stock['ret_stock'] = (stock['Adj Close']/stock['Adj Close'].shift(1))-1
# Merge the two datasets, keep only returns
df = sp[['ret_sp']].merge(stock[['ret_stock']], left_index = True, right_index = True) 
# Add risk free rate (assume constant for simplicity) 
df['rf'] = 0.00001
# We need a constant to run regressions
df['const'] = 1 
df['exret_stock'] = df.ret_stock - df.rf
df['exret_sp'] = df.ret_sp - df.rf
# Remove missing values
df.dropna(inplace=True) 
# Calculate the stock's alpha and Beta
reg = sm.OLS(endog = df['exret_stock'], exog = df[['const', 'exret_sp']], missing = 'drop')
results = reg.fit()
print(results.summary())
alpha = round(results.params['const']*100,3)
beta = round(results.params['exret_sp'],2)
# Print the values of alpha and beta
print(f'The alpha of the stock of {ticker} is {alpha} percent.')
print(f'The beta of the stock of {ticker} is {beta}.')

