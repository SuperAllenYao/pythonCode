#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# 使用split正则分割字符串
content = 'one1two2three3four4five5six6'
p = re.compile(r'\d+')
rest = p.split(content)
print(rest)
