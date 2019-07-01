#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

content = 'hello world'
p = re.compile(r'world')
rest = p.search(content)
print(rest)
