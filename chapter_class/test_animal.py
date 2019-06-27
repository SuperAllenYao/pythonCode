#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BaseCat(object):
    """猫科动物的基础类"""
    tag = "猫科动物"

    def __init__(self, name):
        self.name = name  # 猫都有名称

    def eat(self):
        """猫吃东西"""
        print('猫都要吃东西')


# class ProtectedMixin(object):
#     """受保护的类"""
#
#     def protected(self):
#         print('我是受省份级别保护的')


class Tiger(BaseCat):
    """老虎类 也是猫科动物"""

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def show_info(self):
        print('Tiger: {}, 颜色: {}'.format(self.name, self.color))

    def eat(self):
        # 调用父类的方法
        super().eat()
        print('我还喜欢吃肉,大猪肉')


class Panda(BaseCat):
    """熊猫类 也是猫科动物"""
    pass


class PetCat(BaseCat):
    """家猫类"""

    def eat(self):
        # 调用父类的方法
        super(PetCat, self).eat()
        print('我还喜欢猫粮')


class HuaCat(PetCat):
    """中华田园猫"""

    def eat(self):
        # 调用父类的方法
        super(HuaCat, self).eat()
        print('我还喜欢零食')


class DuanCat(PetCat):
    """英国短毛猫"""

    def eat(self):
        # 调用父类的方法
        print('我啥都吃')


if __name__ == '__main__':
    tiger = Tiger('华南虎', '黄色')
    tiger.show_info()
    tiger.eat()
