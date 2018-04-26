# -*- coding: utf-8 -*-
__author__ = 'Dragon Sun'


import time


class BaseClass:

    @staticmethod
    def cale_elapsed(callback, **kwargs):
        start = time.time()
        ret = callback(**kwargs)
        end = time.time()
        elapsed = end - start

        if isinstance(ret, tuple):
            l = list(ret)
            l.append(elapsed)
            return tuple(l)
        else:
            return ret, elapsed
