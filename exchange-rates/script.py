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
rates = response.json()['rates']

# Map the exchange rates to the orders df
orders['exchange_rate'] = orders['currency'].map(rates, na_action='ignore')

# Create the amount column
orders['amount_usd'] = orders['amount'] * orders['exchange_rate']

# Calculate total sales for the day
total_usd_sales = orders['amount_usd'].sum() 
print(total_usd_sales)

# Preview the new df
print(orders.head())