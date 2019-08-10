#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
import time

test_result = webdriver.Chrome()  # 打开chrome浏览器
test_result = webdriver.PhantomJS()  # 打开PhantomJS浏览器
test_result = webdriver.Firefox()  # 打开Firefox浏览器
test_result.get("https://echarts.baidu.com/examples/")
test_result.maximize_window()
for item in test_result.find_elements_by_xpath("//h4[@class='chart-title']"):
    print(item.text)
print(test_result.title)
time.sleep(5)
test_result.quit()