#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def pow_number(l):
    """
    根据给定的列表数据, 计算里面每一项的立方
    l: list/type int类型的列表或元祖
    return: 原来列表中每一项的立方
    """
    rest_list = []
    for x in l:
        rest_list.append(x * x * x)
    return rest_list


def f(n):
    return n * n * n


def pow_num_use_map(l):
    """
    使用map函数计算给定列表的每一项的立方
    l: list/type int类型的列表或元祖
    return: 原来列表中每一项的立方
    """
    return map(f, l)


def pow_num_use_lambda(l):
    """
    使用map函数/lambda函数计算给定列表的每一项的立方
    l: list/type int类型的列表或元祖
    return: 原来列表中每一项的立方
    """
    return map(lambda n: n * n * n, l)


if __name__ == '__main__':
    clist = [1, 2, 3, 4, 5, 6, 7, 9]
    rest = pow_number(clist)
    print(rest)
    print('---------------------')
    rest_f = pow_num_use_map(clist)
    print(list(rest_f))
    print('---------------------')
    rest_f = pow_num_use_lambda(clist)
    print(list(rest_f))
