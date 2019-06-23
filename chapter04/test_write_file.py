#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from datetime import datetime


def write_file():
    """ 写入文件 """
    file_name = 'chapter04/write_file.txt'
    # 以写入的方式打开文件
    f = open(file_name, 'w')
    # 写入一行内容
    f.write('hello')
    # 换行操作
    f.write('\n')
    # 再写入一行内容
    f.write('world')
    # 关闭文件
    f.close()


def write_mult_lines():
    """ 向文件中写入多行内容 """
    file_name = 'chapter04/write_mult_lines.txt'
    with open(file_name, 'w') as f:
        line = ['第一行', '第二行', '第三行']
        f.writelines(line)


def write_user_log():
    """ 记录用户的日志 """
    # 记录用户ID + 访问时间
    rest = "用户: {0}, 访问时间: {1}".format(random.randint(1000, 9999),
                                       datetime.now())
    # 文件名称
    file_name = 'chapter04/write_user_log.txt'
    with open(file_name, 'a') as f:
        f.write(rest)
        f.write('\n')


def read_and_write():
    """ 先读, 再写入"""
    file_name = 'chapter04/read_and_write.txt'
    with open(file_name, 'r+') as f:
        rest_read = f.read()
        # 如果里面有1, 就写bbb
        # 如果里面没有1, 就写一行数据 aaa
        if '1' in rest_read:
            f.write('bbb')
        else:
            f.write('aaa')
        f.write('\n')


if __name__ == '__main__':
    # write_file()
    # write_mult_lines()
    # write_user_log()
    read_and_write()
