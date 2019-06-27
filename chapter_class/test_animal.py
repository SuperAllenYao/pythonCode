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


class ProtectedMixin(object):
    """受保护的类"""

    def protected(self):
        print('我是受省份级别保护的')


class Tiger(BaseCat, ProtectedMixin):
    """老虎类 也是猫科动物"""

    def eat(self):
        # 调用父类的方法
        super(Tiger, self).eat()
        print('我还喜欢吃肉,大猪肉')


class Panda(BaseCat, ProtectedMixin):
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
    # 实例化中华田园猫
    # cat = HuaCat("小黄")
    # cat.eat()
    # print('-------------------------------------------')
    # # 实例化英国短毛猫
    # cat_d = DuanCat("小辉")
    # cat_d.eat()
    #
    # # 子类的判断
    # print(issubclass(DuanCat, BaseCat))
    # print(issubclass(DuanCat, PetCat))
    # print(issubclass(DuanCat, Tiger))
    panda = Panda('卧龙小熊猫')
    panda.eat()
    panda.protected()

    Tiger = Tiger('华南虎')
    Tiger.protected()
    print('------------------------------------')
    # 验证子类信息
    print(issubclass(Panda, ProtectedMixin))
    # print(issubclass(Tiger, ProtectedMixin))
