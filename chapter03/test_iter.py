#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class PowerNumber(object):
    """
    迭代器
    生成1,2,3,4,5,... 的平方
    """
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value * self.value

    def __iter__(self):
        return self


if __name__ == '__main__':
    pow = PowerNumber()
    # print(pow.__next__())
    # print(pow.__next__())
    # print(pow.__next__())
    # print(next(pow))
    # print(next(pow))
    # print(next(pow))
    for i in pow:
        print(i)
