# -*- coding: utf-8 -*-
__author__ = 'Dragon Sun'


# import psycopg2
import psycopg2.extras
from conf.db_conf import *


_conn = psycopg2.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE)
_cursor = _conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


def get_one(sql, params=None):
    _cursor.execute(sql, params)
    return _cursor.fetchone()


def get_all(sql, params=None):
    _cursor.execute(sql, params)
    return _cursor.fetchall()


def execute(sql, params=None):
    _cursor.execute(sql, params)
    _conn.commit()


# 批量执行
#   command 是一个list，里面的每一个元素是一个字典，代表着一条SQL命令
#   字典的格式为：{'sql': 'sql语句', 'params': (参数列表)}
def batch_execute(cmds):
    for cmd in cmds:
        sql = cmd['sql']
        params = cmd['params']
        _cursor.execute(sql, params)
    _conn.commit()
