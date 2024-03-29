# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:53:47 2024

@author: Suneel
"""


import yfinance as yahooFinance
import pandas as pd

#url = "https://nsearchives.nseindia.com/content/indices/ind_nifty100list.csv"
#s = requests.get(url).content
pd.set_option('display.max_rows', None)

nifty100df = pd.read_csv("G:/Study/Algo_trade/Labs/data/nse/symbols/ind_nifty100list.csv")

nifty100list = nifty100df["Symbol"]

for symbol in nifty100list:
    print(symbol+".NS")
    GetFacebookInformation = yahooFinance.Ticker(symbol+".NS")
    data = pd.DataFrame(GetFacebookInformation.history(period="max"))
    data.to_csv("G:/Study/Algo_trade/Labs/data/nse/nifty100/"+symbol+".csv")
