#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

test = webdriver.Chrome()
# test.maximize_window()
# test.set_window_size(400, 800)
test.get("https://www.baidu.com/")
# # 定位输入框，并发送python
# test.find_element_by_xpath("//input[@id='kw']").send_keys("python")
# # 定位到按钮，并点击
# test.find_element_by_xpath("//input[@id='su']").click()
time.sleep(2)
test.get("https://news.baidu.com/")
time.sleep(2)
test.refresh()
time.sleep(2)
# # 打印浏览器标签标题
# print(test.title)
# # 打印网页源码
# print(test.page_source)
# # 打印浏览器cookies
# print(test.get_cookies())
test.quit()