#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import os.path


class FileBackup(object):
    """
    文本文件备份
    """

    def __init__(self, src, dist):
        """
        构造方法
        参数 src: 目录, 需要备份的文件目录
        参数 dist: 目录, 备份后的文件目录
        """
        self.src = src
        self.dist = dist

    def read_file(self):
        """ 读取src目录下的所有文件 """
        ls = os.path(self.src)
        print(ls)
        for l in ls:
            self.back_file(l)

    def back_file(self, file_name):
        """处理备份"""
        pass


if __name__ == '__main__':
    # # 要备份的文件目录地址
    # src_path = '/Users/superallen/Desktop/src'
    # # 备份后的文件目录地址
    # dist_path = '/Users/superallen/Desktop/dist'
    # bak = FileBackup()

    # 要备份的文件目录地址
    src_path = os.path.abspath(__file__)
    print(src_path)
    # 备份后的文件目录地址
    dist_path = '/Users/superallen/Desktop/dist'
    bak = FileBackup()
