#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from datetime import datetime
import random

def gen_trans_id(date=None):
    """
    根据交易时间得到一个唯一的交易流水ID
    date: 日期
    return: 交易流水ID
    """
    #如果没有传入时间, 则使用系统当前时间
    if date is None:
        date = datetime.now()
    #为了保证此交易ID的唯一性, 在此使用 日期+时间+毫秒+随机数(6位) 的方案
    return '{0}{1}'.format(date.strftime('%Y%m%d%H%M%S%f'), random.randint(100000, 999999))
    # return date.strftime('%Y%m%d%H%M%S%f') + str(random.randint(100000, 999999))
