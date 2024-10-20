# Import required packages/libraries
import pandas as pd
import requests
import json

# Read the CSV file into a DataFrame
orders = pd.read_csv('exchange-rates/data/orders-2024-01-21.csv')

# Define a function to get the exchange rate
def get_exchange_rate(json_data: dict, key: str) -> float:
    """Return the exchange rate by accessing the rate from a dictionary"""
    return json_data['rates'][key]
    
# Define a function to get the amount in USD
def calc_usd(amount: float, exchange_rate: float) -> float:
    """Converts a currency to USD based on a given exchange rate"""
    return amount * exchange_rate


# Define parameters
params = {'base':'USD', 'date':'2024-01-21'}

# Query the url
response = requests.get('https://api.vatcomply.com/rates', params=params)

# Transform the response text to a dictionary
rates = response.json()

# Create empty lists to store our new columns
exchange_rate = []
amount_usd = []

# Apply the functions to the df and append to the lists
for row in orders.itertuples(index=False):
    exchange_rate.append(get_exchange_rate(rates, row.currency))

orders['exchange_rate'] = exchange_rate

for row in orders.itertuples(index=False):
    amount_usd.append(calc_usd(row.amount, row.exchange_rate))

orders['amount_usd'] = amount_usd

# Calculate total sales for the day
total_usd_sales = orders['amount_usd'].sum() 

# Preview the new df
print(orders.head())