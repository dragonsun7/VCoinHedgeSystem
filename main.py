# -*- coding: utf-8 -*-
__author__ = 'Dragon Sun'


from exchanges.exchange_okex import *


okex = OKExExchange('13980660107')
asks, bids, elapsed = okex.cale_elapsed(okex.get_depth, pair='BTC_USDT')
print(asks)
print(bids)
print(elapsed)
