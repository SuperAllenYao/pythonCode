#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 显示等待
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# test = webdriver.Chrome()
# test.maximize_window()
# test.get("https://www.baidu.com/")
# #WebDriverWait 设置显示等待
# # 1，浏览器对象。2，超时参数。3，轮询参数。
# # unitl,EC场景判断，通过ID来找相关的元素
# ele = WebDriverWait(test, 5,
#                     0.5).until(EC.presence_of_element_located((By.ID, "kw")))
# ele.send_keys("python")
# time.sleep(2)
# test.quit()

# 隐式等待
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

test = webdriver.Chrome()
# 设置隐式等待为5秒，在5秒内不断轮询是否定位到了元素，如没有则抛出异常
test.implicitly_wait(5)
test.get("https://www.baidu.com/")
try:
    test.find_element_by_id('kw').send_keys("python")
    time.sleep(2)
except NoSuchElementException as e:
    print(e)
test.quit()