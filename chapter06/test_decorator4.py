#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def log(Name=None):
    """ 记录函数执行的日志 """

    def decorator(func):
        def warpper(*args, **kwargs):
            print('-------{}.start-------'.format(Name))
            rest = func(*args, **kwargs)
            print('------{}.end------'.format(Name))
            return rest
        return warpper
    return decorator


@log('Hello')
def hello():
    """ 简单功能模拟 """
    print('Hello World')


if __name__ == '__main__':
    print('doc:{}'.format(hello.__doc__))
    print('name:{}'.format(hello.__name__))
    hello()
