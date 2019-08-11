from selenium import webdriver
# 导入相关的包
from selenium.webdriver.common.action_chains import ActionChains
import time

test = webdriver.Chrome()
test.maximize_window()
test.get("https://www.baidu.com/")
# 找到“设置”这个标签
settings = test.find_element_by_link_text("设置")
# test当作参数传入，然后移动到相关的元素，最后执行
ActionChains(test).move_to_element(settings).perform()
time.sleep(5)
test.quit()