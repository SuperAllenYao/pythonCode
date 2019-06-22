#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 函数的使用技巧2
# 1. 序列传参
def calc(a, b, c):
    return (a+b)*c


l = [1, 5, 10]
print(calc(*l))


def heath_check(name, age, height, weight, hr, hbp, lbp, glu):
    print('您的健康状况良好')


heath_check(name='Allen', age=26, height=170,
            weight=140, hr=100, hbp=90, lbp=100, glu=20)

# 2. 字典传参


def heath_check1(name, age, *, height, weight, hr, hbp, lbp, glu):
    print('您的健康状况良好')


param = {"name": "张三", "age": 26, "height": 170,
         "weight": 140, "hr": 130, "hbp": 23, "lbp": 45, "glu": 11}

heath_check(**param)

# 3. 返回值包含多个数据

def get_detil_info():
	