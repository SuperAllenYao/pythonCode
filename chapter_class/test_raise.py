#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MyExcpetion(Exception):
    """自定义的异常类"""
    pass


def v_for():
    """ 自定义函数 """
    for i in range(1, 100):
        if i == 20:
            raise MyExcpetion()
        print(i)


def call_v_for():
    """ 调用v_for函数 """
    print('开始调用v_for')
    try:
        v_for()
    except MyExcpetion:
        print('发现错误--------------')
    print('结束调用')


def test_raise():
    print('测试函数')
    call_v_for()
    print('测试完毕')


if __name__ == '__main__':
    test_raise()
