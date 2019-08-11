from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from lxml import etree
import time


class WebDriver(object):
    def __init__(self):
        super(WebDriver, self).__init__()
        # opt = Options()
        # 设置为无头
        # opt.add_argument('--headless')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def handle_job(self):
        self.driver.get(
            "https://search.51job.com/list/000000,000000,0000,00,9,99,%2520,2,1.html"
        )
        if WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
                EC.presence_of_element_located((By.ID, "kwdselectid"))):
            input_kw = input("\t请输入要查找的岗位信息：")
            self.driver.find_element_by_id("kwdselectid").send_keys(input_kw)
            self.driver.find_element_by_class_name("p_but").click()
            if WebDriverWait(self.driver, 5, poll_frequency=0.5).until(
                    EC.presence_of_element_located((By.ID, "resultList"))):
                while True:
                    self.parse_html(self.driver.page_source)
                    if self.driver.find_element_by_xpath(
                            "//li[@class='bk'][2]/a").text == "下一页":
                        self.driver.find_element_by_xpath(
                            "//li[@class='bk'][2]/a").click()
                    else:
                        break
            self.driver.quit()
            # time.sleep(5)
            # self.driver.quit()

    def parse_html(self, page_source):
        data = etree.HTML(page_source)
        all_div = data.xpath("//div[@id='resultList']//div[@class='el']")
        info_list = []
        for item in all_div:
            info = {}
            # . 代表的是使用item下的Xpath语句
            # 获取数据的时候，要使用列表索引为0的数据
            # 插入工作名称数据
            info['jobname'] = item.xpath("./p/span/a/@title")[0]
            # 插入公司名称数据
            info['company_name'] = item.xpath(
                ".//span[@class='t2']/a/@title")[0]
            # 插入公司地区数据
            info['company_address'] = item.xpath(
                ".//span[@class='t3']/text()")[0]
            # 此字段数据有为空的情况，所以需要现判断下抓过来的是不是为空
            temp = item.xpath(".//span[@class='t4']/text()")
            if len(temp) == 0:
                # 为空则插入“无”
                info['money'] = "无"
            else:
                # 不为空则插入爬回来的数据
                info['money'] = item.xpath(".//span[@class='t4']/text()")[0]
            # 插入发布日期数据
            info['date'] = item.xpath(".//span[@class='t5']/text()")[0]
            print(info)
        info_list.append(info)
        # return info_list


test = WebDriver()
test.handle_job()