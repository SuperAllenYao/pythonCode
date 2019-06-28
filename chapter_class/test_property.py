#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class PetCat(object):
    """家猫类"""

    def __init__(self, name, age):
        """
        构造方法
        参数 name: 猫的名称
        参数 age: 猫的年龄
        """
        self.name = name
        # 私有属性,不能随意改变
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, v):
        if not isinstance(v, int):
            print('年龄只能是整数')
            return 0
        if v < 0 or v > 100:
            print('年龄只能介于0-100之间')
            return 0
        self.__age = v

    @property
    def show_info(self):
        """显示猫的信息"""
        return "我叫: {}, 今年{}岁".format(self.name, self.age)

    def __str__(self):
        return self.show_info()


if __name__ == '__main__':
    cat_black = PetCat('小黑', 1)
    rest = cat_black.show_info
    print(rest)
    # 改变猫的年龄
    cat_black.age = 6
    rest = cat_black.show_info
    print(rest)
    # print(cat_black)
