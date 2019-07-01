#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# 找出以下字符串中的数字
content = 'one1two2Three3four444five5'
# 使用编译的对象
p = re.compile(r'[a-z]+', re.I)
rest = p.findall(content)
print(rest)
print('------------------------------------')
# 不编译
rest = re.findall(r'[a-z]+', content, re.I)
print(rest)
