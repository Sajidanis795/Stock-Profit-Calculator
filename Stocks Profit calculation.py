#!/usr/bin/env python
# coding: utf-8

# In[2]:


import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime

# Define the list of stock symbols
stock_symbols = ['AAPL', 'GOOG', 'MSFT', 'MUV2.DE' , 'SPY']

# Define the date range
start_date = datetime(2018, 1, 1)  # Set your start date (Year, Month, Day)
end_date = datetime(2023, 6, 19)  # Set your end date (Year, Month, Day)

# Define the number of shares bought
shares_bought = 100

# Create a dictionary to store the stock data
stock_data = {}

# Create lists to store the stock symbols and profits for the plot
symbols = []
profits = []

# Loop through the stock symbols and fetch the data
for symbol in stock_symbols:
    data = yf.download(symbol, start=start_date, end=end_date)
    stock_data[symbol] = data

# Calculate the profit for each stock
for symbol, data in stock_data.items():
    # Get the price at which the stock was bought and sold
    buy_price = data['Close'][0]
    sell_price = data['Close'][-1]

    # Calculate the profit
    profit = (sell_price - buy_price) * shares_bought

    # Append the symbol and profit to the lists
    symbols.append(symbol)
    profits.append(profit)

    print(f'Profit for {symbol}: {profit:.2f}')

# Create a bar chart
fig = go.Figure(data=[go.Bar(x=symbols, y=profits)])

# Add titles
fig.update_layout(title_text='Profit for Stocks', xaxis_title='Stock Symbol', yaxis_title='Profit')

# Show the plot
fig.show()

