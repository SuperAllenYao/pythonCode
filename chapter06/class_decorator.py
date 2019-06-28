#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def f(self):
    print("{}.要吃东西".format(self.name))
    print('00000000000')


def eat(cls):
    """ 吃东西装饰器 """
    # cls.eat = lambda self: print("{}.要吃东西".format(self.name))
    cls.eat = f
    return cls


@eat
class Cat(object):
    """ 猫类 """

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    cat = Cat('小黑')
    cat.eat()
