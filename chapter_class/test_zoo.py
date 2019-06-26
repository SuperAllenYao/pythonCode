#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class cat(object):
    """
    猫科动物类
    """
    tag = "我是家猫"

    def __init__(self, name, age, sex=None):
        self.name = name
        self.__age = age
        self.sex = sex

    def set_age(self, age):
        """
        改变猫的年龄
        参数 age: 猫的年龄 int
        """
        self.__age = age
        # return self.__age

    def show_info(self):
        """
        显示猫的信息
        return: 猫的信息
        """
        rest = '这只小猫的名字是: {0}, 今年{1}岁'.format(self.name, self.__age)
        print('我的性别{0}'.format(self.sex))
        print(rest)
        return rest

    def eat(self):
        """ 吃 """
        print("猫喜欢吃鱼")

    def catch(self):
        """猫喜欢抓老鼠"""
        print("我能抓老鼠")


class Tiger():
    pass


if __name__ == '__main__':
    # 实例化你家的小黑
    cat_black = cat("小黑", 2, "公的")
    cat_black.eat()
    cat_black.show_info()
    print('-----------------------')
    print(cat_black.name)
    # print(cat_black.__age)  # 无法访问, 私有变量
    # 更改猫的名称
    cat_black.name = "黑黑"  # 可以直接改变
    cat_black.show_info()
    cat_black.__age = 6     # 无法操作私有变量

    print('------------------------')
    cat_black.set_age(7)
    cat_black.show_info()

    print('------------------------')
    print(cat.tag)
    print(cat_black.tag)

    print('------------------------')
    # 实例化我家的小白
    cat_withe = cat("小白", 3, '母的')
    cat_withe.show_info()
    print(cat_withe.tag)

    # 类的实例判断
    print(isinstance(cat_black, cat))
    print(isinstance(cat_withe, cat))
    print(isinstance(cat_black, Tiger))
    print(isinstance(cat_withe, Tiger))
