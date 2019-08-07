#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

url = "http://httpbin.org/ip"
# 使用verify关键字关闭证书验证
result = requests.get(url=url, verify=False)
print(result.text)
