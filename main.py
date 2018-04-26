# -*- coding: utf-8 -*-
__author__ = 'Dragon Sun'


from exchanges.okex import *
from exchanges.huobi import *


USERNAME = '13980660107'
PAIR = 'BTC_USDT'
BUY_MARKET = 'okex'
SELL_MARKET = 'huobi'

okex = OKExExchange(USERNAME)
asks, bids, elapsed = okex.cale_elapsed(okex.get_depth, pair=PAIR)

huobi = HuobiExchange(USERNAME)
asks, bids, elapsed = huobi.cale_elapsed(huobi.get_depth, pair=PAIR)


print(asks)
print(bids)
print(elapsed)
