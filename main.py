from config import *
import json
import alpaca_trade_api as tradeapi
#paper trading

def stonks_high(request):
    api = tradeapi.REST(API_KEY_ID, API_SECRET_KEY, BASE_URL)
    #account = api.get_account()
    #account.get_json
    order = api.submit_order('GOOG', 8, 'buy', 'market', 'gtc')
    print(order)
    return 'poop'
    #act_dict = json.load(account)
 