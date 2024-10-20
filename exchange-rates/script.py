# Import required packages/libraries
import pandas as pd
import requests


# Read the CSV file into a DataFrame
orders = pd.read_csv('exchange-rates/data/orders-2024-01-21.csv')

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