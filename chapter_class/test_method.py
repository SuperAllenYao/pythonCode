#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Cat(object):
    tag = '猫科动物'

    def __init__(self, name):
        self.name = name

    @staticmethod
    def breath():
        """ 呼吸 """
        print('猫都需要呼吸')

    @classmethod
    def show_info(cls):
        """展示猫的信息"""
        print("类的属性: {}, 实例的属性: {}".format(cls.tag, cls.name))


if __name__ == '__main__':
    # 通过类调用
    Cat.breath()
    cat = Cat('小黑')
    # 通过类的实例调用
    cat.breath()
    cat.show_info()
