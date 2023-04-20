import alpaca_trade_api as tradeapi
from alpaca_trade_api import TimeFrame

import os
import pandas as pd
from dotenv import load_dotenv


load_dotenv()


api_key = os.getenv('API_KEY')
secret_key =os.getenv('SECRET_KEY')
endpoint = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(api_key, secret_key, endpoint, api_version='v2')

def simple_moving_average(data, window):
    return data.rolling(window=window).mean()

symbol= input('Insert Symbol: ')
timeframe='1D'
start_date='2023-01-01'
end_date='2023-04-19'
window=10

# Fetch historical price data
bars= api.get_bars(symbol,timeframe, start=start_date, end=end_date).df

# Extract close prices and create a Pandas Series
close_prices = bars['close']  

# Calculate the Simple Moving Average (SMA)
sma = simple_moving_average(close_prices, window)

print(sma)
