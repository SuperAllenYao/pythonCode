#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Cat(object):
    """"""

    def __init__(self):
        print("对象产生了: {}".format(id(self)))

    def __del__(self):
        print("对象删除了: {}".format(id(self)))


def f0():
    while True:
        c1 = Cat()


def f1():
    while True:
        l = []
        c1 = Cat()
        l.append(c1)


if __name__ == '__main__':
    # f0()
    f1()
