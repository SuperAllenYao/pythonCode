#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def log(func):
    """ 记录函数执行的日志 """

    def warpper():
        print('-------start-------')
        func()
        print('------end------')

    return warpper


@log
def hello():
    """ 简单功能模拟 """
    print('Hello World')


if __name__ == '__main__':
    hello()
