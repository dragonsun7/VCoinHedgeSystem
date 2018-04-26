# -*- coding: utf-8 -*-
__author__ = 'Dragon Sun'


from exchanges.base import *


class HuobiExchange(BaseExchange):

    def __init__(self, username):
        BaseExchange.__init__(self, username)

    def use_proxy(self):
        return True

    def get_symbol(self):
        return 'huobi'

    def convert_pair(self, pair):
        return str(pair).replace('_', '')

    def get_depth(self, pair):
        url = 'https://api.huobipro.com/market/depth'
        params = {
            'symbol': self.convert_pair(pair).lower(),
            'type': 'step1'
        }

        json = self.request(HTTP_METHOD_GET, url, params)
        if json['status'] != 'ok':
            return [], []
        asks = json['tick']['asks']
        bids = json['tick']['bids']
        return asks, bids
