import finnhub 
import datetime 
import time 
import pandas as pd

class getData:

    def __init__(self):
        pass 

    '''
    Function to calculate a given number of days in unix
    '''
    def getUnix(self, days):
        return days * 86400

    '''
    Gather data from Finnhub into a dataframe
    '''
    def assembleDF(self, ticker):
        apiKey = 'cc06epiad3idf21ispa0'
        client = finnhub.Client(api_key = apiKey)
        today = int(time.time())
        data = client.stock_candles(ticker, 'D', today - self.getUnix(365), today)
        df = pd.DataFrame.from_dict(data)
        df = df.dropna()
        df['Date'] = [datetime.datetime.fromtimestamp(i, tz= None) for i in data['t']]
        df = df.groupby('Date').sum()
        df = df.asfreq(freq ='D')
        df['c'] = df['c'].ffill()
        df = df[['c']]
        df.index.freq = 'D'
        df.to_csv(f'{ticker}data.csv')
        return df

