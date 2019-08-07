#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

# 设置代理数据，隐藏真实ip
proxy = {"http": "http://用户名:密码@代理地址:端口号", "https": "http://用户名:密码@代理地址:端口号"}

url = "http://httpbin.org/ip"
for i in range(5):
    # 设置代理，使用proxies关键字
    result = requests.get(url=url, proxies=proxy)
    print(result.text)
