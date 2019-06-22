#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 函数的使用技巧
# 1. 为形参数设置默认参数的时候，只需要在形参后加=和默认值即可

def exchage(amt, scoure="CNY", tagert="USD"):
    if scoure == "CNY" and tagert == "USD":
        result = amt / 6.75
        return result
    elif scoure == "CNY" and tagert == "EUR":
        result = amt / 7.7512
        return result
    else:
        none = '无对应货币'
        return none

# 2.以形参数形式传参(关键字传参)


def heath_check(name, age, height, weight, hr, hbp, lbp, glu):
    print('您的健康状况良好')

heath_check(name='Allen', age=26, height=170,
            weight=140, hr=100, hbp=90, lbp=100, glu=20)

# 3. 要求使用关键字传参加*，*号后面的参数必须用关键字来传参
def heath_check1(name, age, *, height, weight, hr, hbp, lbp, glu):
    print('您的健康状况良好')