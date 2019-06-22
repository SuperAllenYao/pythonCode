#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = input("Enter file:")  # 输入文件名
handle = open(name)  # 将文件名用作把手
adress = list()  # 空的列表
time = dict()  # 空的字典
for line in handle:  # 拿出每一行文字
    line = line.split()  		# 将此行文字的空格去掉,并转换为list
    if 'From' in line:  		# 判断此行是否为“From”开头
        adress.append(line[1])  # 将[1]位置的数据添加到adress中
    else:
        continue  # 跳出此次循环
for word in adress:  # 循环每一个adress的数据
    time[word] = time.get(word, 0) + 1  # 新建key,value

# 计算谁最大
name = None
count = None
for k, v in time.items():  # 将time字典中的key,value拿出来到k和v
    if count is None or v > count:
        name = k
        count = v
print(name, count)
