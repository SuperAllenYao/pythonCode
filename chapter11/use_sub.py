#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# 使用sub正则进行字符替换
content = 'one1two2three3333four4five5six6'
# 使用正则替换
p = re.compile(r'\d+')
rest = p.sub('#', content)
print(rest)

# 使用正则表达式更换字符串位置
s2 = 'hello world!'
p2 = re.compile(r'(\w+) (\w+)')
rest_pos = p2.sub(r'\2 \1', s2)
print(rest_pos)

# 在原有的基础上替换并改变内容


def f(m):
    """ 使用函数进行替换规则改变 """
    return m.group(2).upper() + ' ' + m.group(1)


rest_c = p2.sub(f, s2)
print(rest_c)
# 使用匿名函数进行替换 lambda
rest_lamb = p2.sub(lambda m: m.group(2).upper() + ' ' + m.group(1), s2)
print('----------------------------')
print(rest_lamb)
