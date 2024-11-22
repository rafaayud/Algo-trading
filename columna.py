import pandas as pd
df = pd.read_csv('sp500.csv')

a = df['Symbol']
a.to_csv('Tickers',index=False)

portfolio_size = input("Enter the value of your portfolio: ")

try:
    