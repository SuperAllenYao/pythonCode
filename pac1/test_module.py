#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from datetime import datetime
from pac1.trans.tools import gen_trans_id
from pac1.work.tools import getFlieType


def test_trans_tool():
    # 测试 trans 包下的 tools 模块
    id1 = gen_trans_id()
    print(id1)
    date = datetime(2015, 10, 1, 13, 13, 13)
    id2 = gen_trans_id(date)
    print(id2)


def test_work_tools():
    # 测试work模块
    f_name = "/Users/superallen/Desktop/Screen Shot 2019-06-21 at 19.43.47.png"
    fname = getFlieType(f_name)
    print(fname)


if __name__ == '__main__':
    test_trans_tool()
    test_work_tools()
