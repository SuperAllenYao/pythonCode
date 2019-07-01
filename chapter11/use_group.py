#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def test_group():
    content = 'hello world!'
    p = re.compile(r'world')
    rest = p.search(content)
    print(rest)
    if rest:
        # group的使用
        print(rest.group())
        # groups的使用
        print(rest.groups())


def test_id():
    """ 身份证号码正则匹配 """
    # p = re.compile(r'(\d{6})(\d{4})((\d{2})(\d{2}))\d{2}(\d{1})([0-9]|X)')
    p = re.compile(r'(\d{6})(?P<year>\d{4})((?P<month>\d{2})(?P<day>\d{2}))\d{2}(\d{1})([0-9]|X)')
    id1 = '430656199610015493'
    id2 = '43065619961001548X'
    rest1 = p.search(id2)
    # 月、日
    print(rest1.group(4))
    print(rest1.group(5))
    # groups的使用
    print(rest1.groups())
    # groupdict的使用
    print(rest1.groupdict())


if __name__ == '__main__':
    # test_group()
    test_id()
