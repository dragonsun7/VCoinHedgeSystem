# -*- coding: utf-8 -*-
__author__ = 'Dragon Sun'


from exchanges.base import *


class OKExExchange(BaseExchange):

    def __init__(self, username):
        BaseExchange.__init__(self, username)

    def use_proxy(self):
        return True

    def get_symbol(self):
        return 'okex'

    def get_depth(self, pair):
        url = 'https://www.okex.com/api/v1/depth.do'
        params = {
            'symbol': str(pair).lower(),
            'size': 200
        }

        json = self.request(HTTP_METHOD_GET, url, params)
        asks = sorted(json['asks'], reverse=False)
        bids = sorted(json['bids'], reverse=True)
        return asks, bids
