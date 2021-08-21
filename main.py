from config import *
import alpaca_trade_api as tradeapi
import json
import numpy as np
import time
import pathlib
import pandas as pd
from stonk_indicator import Trend0
from td.client import TDClient
from td.utils import TDUtilities

def testcloud(self):
    sym = "SPY"

    api = tradeapi.REST(API_KEY_ID,API_SECRET_KEY, BASE_URL)

    #Initalize, validate token, login, and create session
    TDSession = TDClient(
        client_id = TD_CLIENT_ID,
        redirect_uri = REDIRECT_URL,
        credentials_path = "/Users/Jason/Desktop/Code/stonks/stonks.json"
    )
    TDSession.validate_token()
    TDSession.login()

    #get times and last 12 hrs
    end_time = int(time.time() * 1000)
    start_time = end_time - 36000000
    #early prices top, use the open as the price for the hour
    prices = TDSession.get_price_history(symbol = sym, period_type = 'day', start_date = start_time, end_date = end_time, frequency_type = 'minute', frequency = '60')
    current_quote = TDSession.get_quotes([sym])
    latest = {
        "datetime": current_quote[sym]['regularMarketTradeTimeInLong'],
        "open": current_quote[sym]['lastPrice']
    }
    prices['candles'].append(latest)
    #prices = prices['candles']
    #return str(time.strftime("%m, %d, %Y",t))
    #do testing on getting market data and somehow put some prices into a numpy array to work with

    list = np.array([]) #temp
    indicator = Trend0(
        name = 'trend0',
        period = 10,
        exponent = 1.5,
        prices = list
    )

    #main
    if list.get_value > 0 and len(api.list_positions())  <= 0:
        order = api.submit_order(symbol = sym, qty = 300, side = 'buy', time_in_force = "day")
    if list.get_value < 0 and len(api.list_positions())  >= 0:
        order = api.submit_order(symbol = sym, qty = 300, side = 'sell', time_in_force = "day")

    return str(len(api.list_positions()))

 