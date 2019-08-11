#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
import time

test_result = webdriver.Chrome()  # 打开chrome浏览器
test_result = webdriver.PhantomJS()  # 打开PhantomJS浏览器
test_result = webdriver.Firefox()  # 打开Firefox浏览器
# 发送请求
test_result.get("https://echarts.baidu.com/examples/")
test_result.maximize_window()  # 将浏览器窗口最大化
# 选中所有标题并输出
for item in test_result.find_elements_by_xpath("//h4[@class='chart-title']"):
    print(item.text)
# 输出当前浏览器标签页的title
print(test_result.title)
time.sleep(5)  # 等待5秒
test_result.quit()  # 退出浏览器
