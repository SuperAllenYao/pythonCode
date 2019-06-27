#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Point(object):
    # 自定义Point类的构造(初始化)方法
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 自定义Point类对象的格式化输出函数(string())
    def string(self):
        a = '该图形初始化点为: {' + 'X:{}, Y:{}'.format(self.x, self.y) + '}; '
        return a


class Circle(Point):
    # 自定义Circle类的构造(初始化)方法
    def __init__(self, x, y, radius):
        Point.__init__(self, x, y)
        self.radius = radius

    # 自定义Circle类对象的格式化输出函数(string())
    def string(self):
        v = super(Circle, self).string()
        print("{}".format(v) + "{" + "半径为:{}".format(self.radius) + "}")


class Size(object):
    # 自定义Size类的构造(初始化)方法
    def __init__(self, w, h):
        self.h = h
        self.w = w
    # 自定义Size类对象的格式化输出函数(string())

    def string(self):
        a = "长宽分别为: {" + "Width:{}, Height:{}".format(self.w, self.h) + "}"
        return a


class Rectangle(Point, Size):

    # 自定义Rectangle类的构造(初始化)方法，并在方法中调用父类的初始化方法以完成初始化
    def __init__(self, x, y, w, h):
        Point.__init__(self, x, y)
        Size.__init__(self, w, h)

    # 自定义Rectangle类对象的格式化输出函数(string())
    def string(self):
        print("{}{}".format(super(Rectangle, self).string(), super(Point, self).string()))


if __name__ == "__main__":
    # 实例化Circle对象，圆心为（5,5），半径为8
    c = Circle(5, 5, 8)
    c.string()
    # 实例化Rectangle对象，顶点位置（15,15），长和宽分别为15和15
    r1 = Rectangle(15, 15, 15, 15)
    r1.string()
    # 实例化Rectangle对象，顶点位置（40,30），长和宽分别为11和14
    r2 = Rectangle(40, 30, 11, 14)
    r2.string()
