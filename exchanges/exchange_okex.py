# -*- coding: utf-8 -*-
__author__ = 'Dragon Sun'


import requests
from conf.http_conf import *
from exchanges.exchange import *


HTTP_METHOD_GET = 'GET'
HTTP_METHOD_POST = 'POST'


class OKExExchange(BaseExchange):

    def __init__(self, username):
        BaseExchange.__init__(self, username)

    def get_symbol(self):
        return 'okex'

    def get_depth(self, pair, count=0):
        url = 'https://www.okex.com/api/v1/depth.do'
        params = {
            'symbol': str(pair).lower(),
        }
        if count > 0:
            params['size'] = count

        json = self.request(HTTP_METHOD_GET, url, params)
        asks = sorted(json['asks'], reverse=False)
        bids = sorted(json['bids'], reverse=True)
        return asks, bids

    # noinspection PyMethodMayBeStatic
    def request(self, method, url, params):
        if HTTP_METHOD_GET == method:
            return requests.get(url, params, proxies=PROXIES).json()
        else:
            return requests.post(url, params, proxies=PROXIES).json()
