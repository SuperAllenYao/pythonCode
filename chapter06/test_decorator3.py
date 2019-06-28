#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def log(Name=None):
    """ 记录函数执行的日志 """

    def decorator(func):
        def warpper():
            print('-------{}.start-------'.format(Name))
            func()
            print('------{}.end------'.format(Name))
        return warpper
    return decorator


@log()
def hello():
    """ 简单功能模拟 """
    print('Hello World')


if __name__ == '__main__':
    hello()
