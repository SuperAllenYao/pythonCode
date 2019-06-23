#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def read_file():
    """ 读取文件 """
    # 相对路径
    file_name = 'chapter04/test.txt'
    # 绝对路径
    # file_path = '/Users/superallen/Desktop/myPyhotnCode/chapter04/test.txt'

    # 使用普通的方式来打开文件
    f = open(file_name)

    # 读文件开头的两个字
    # rest = f.read(2)
    # print(rest)
    # 接着再读取两个字
    # rest1 = f.read(2)
    # print(rest1)
    # 记得关闭文件

    # 按行读取
    # rest = f.readline()
    # print(rest)

    # 读取全部行, 并返回一个列表
    rest = f.readlines()
    print(rest)

    f.close()


if __name__ == '__main__':
    read_file()
