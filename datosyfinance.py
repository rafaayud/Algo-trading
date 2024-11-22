import yfinance as yf
import pandas as pd
import math

stocks = pd.read_csv('Tickers.csv')

def precio_accion(ticker):
    try:
        Ticker = yf.Ticker(ticker)
        price = Ticker.history(period='1d')['Close'][-1]
        return price
    
    except Exception as e:
        print('error')
        return None
    
def market_cap(ticker):
    try:

        Ticker = yf.Ticker(ticker)
        marketcap = Ticker.info.get('marketCap')
        return marketcap
    
    except Exception as e:
        print('error')
        return None

stocks['Stock price'] = stocks['Ticker'].apply(precio_accion)
stocks['Market Cap'] = stocks['Ticker'].apply(market_cap)

number = float(input("Size of the portfolio: "))

def numberStocks(row):
    try:
        
        if pd.isna(row['Stock price']):
            print(f"Datos faltantes para {row['Ticker']}.")
            return None 

        moneyForEach = number / len(stocks)
        
        num = math.floor(moneyForEach / row['Stock price'])
        return num
    
    except Exception as e:
        print(f"Error en {row['Ticker']}: {e}")
        return None

stocks['Number of shares to buy'] = stocks.apply(numberStocks, axis=1)

stocks.to_excel('tablasp500final.xlsx', sheet_name='Stocks to buy', index=False)


















