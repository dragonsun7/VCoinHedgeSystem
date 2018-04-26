# -*- coding: utf-8 -*-
__author__ = 'Dragon Sun'


import requests
import utils.db as db
from base_class import *
from conf.http_conf import *


HTTP_METHOD_GET = 'GET'
HTTP_METHOD_POST = 'POST'


class BaseExchange(BaseClass):

    # ---------------------------------------- 需要重载的方法 ---------------------------------------- #

    def __init__(self, username):
        self.symbol = self.get_symbol()
        self.username = username
        user_info = self._get_user_info()
        self.api_key = user_info['api_key']
        self.secret_key = user_info['secret_key']

    # noinspection PyMethodMayBeStatic
    def use_proxy(self):
        """
        返回是否需要使用代理服务器
        :return: 默认False
        """
        return False

    # noinspection PyMethodMayBeStatic
    def get_symbol(self):
        return ''

    # noinspection PyMethodMayBeStatic
    def convert_pair(self, pair):
        """
        转换交易对的格式
        :param pair: 标准交易对格式(CurrA_CurrB)
        :return: 对应交易所的交易对格式
        """
        return pair

    # noinspection PyMethodMayBeStatic
    def get_depth(self, pair):
        """
        获取指定交易对的市场深度(盘口)
        :param pair: str, 交易对，需要符合currA_currB这样的格式
        :return: tuple，第一个为asks(价格升序)，第二个为bids(价格降序)，每个元素都为：[price, amount]
                        asks和bids的0元素分别为卖一和买一，离盘口越远，索引值越大，asks的价格越高，bids的价格越低
        """
        return [], []

    # ---------------------------------------- 私有方法 ---------------------------------------- #

    # noinspection PyMethodMayBeStatic
    def request(self, method, url, params):
        use_proxy = self.use_proxy()
        if HTTP_METHOD_GET == method:
            if use_proxy:
                return requests.get(url, params, proxies=PROXIES).json()
            else:
                return requests.get(url, params).json()
        else:
            if use_proxy:
                return requests.post(url, params, proxies=PROXIES).json()
            else:
                return requests.post(url, params).json()

    def _get_user_info(self):
        """
        获取必要的用户信息
        :return: 信息字典
        """
        sql = '''
SELECT
  u.api_key,
  u.secret_key
FROM
  bs_exchange_user AS u,
  bs_exchange as e
WHERE
  u.exchange_id = e.uid
  AND e.active
  AND u.active
  AND e.symbol = %s
  AND u.username = %s
        '''
        params = [self.symbol, self.username]
        return db.get_one(sql, params)
