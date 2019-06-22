#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


def use_reduce(l):
    """
    使用reduce + lambda函数进行求和
    l: 列表/元祖
    return:
    """
    return reduce(lambda x, y: x + y, l)


if __name__ == '__main__':
    pass
    list = [1, 2, 4, 6, 7, 8, 9]
    rest = use_reduce(list)
    print(rest)
