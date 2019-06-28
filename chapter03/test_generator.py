#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def pow():
    yield 1
    yield 2
    yield 3
    yield 4


def pow_num1():
    return (x * x for x in [1, 2, 3, 4, 5])


def pow_num2():
    for x in [1, 2, 3, 4, 5]:
        yield x * x


if __name__ == '__main__':
    # rest = pow()
    # print(next(rest))
    # print(next(rest))
    # for i in rest:
    # print(i)
    rest = pow_num2()
    print(rest.__next__())
    print(next(rest))
