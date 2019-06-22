#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re  # 导入re包
sum = 0
handle = open("/Users/superallen/Desktop/regex_sum_206727.txt",
              "r")  # 打开指定文件，并读取
for lines in handle:
    line = lines.rstrip()  # 去掉空格
    nums = re.findall('[0-9]+', line)  # 在line中查找多位字符，并撤出一个list
    for numStr in nums :
        numInt = int(numStr)  # 将for出来的numStr转成int类型
        sum += numInt  # 加起来
print(sum)
