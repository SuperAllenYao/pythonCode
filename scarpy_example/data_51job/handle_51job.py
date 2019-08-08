#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from multiprocessing import Queue
from lxml import etree
import threading
from pymongo import MongoClient
from scarpy_example.data_51job.mongo_db import insert_data


# 处理页面类
class CrawlPage(threading.Thread):
    def __init__(self, thread_name, page_queue, data_queue):
        super(CrawlPage, self).__init__()
        # 线程的名称
        self.thread_name = thread_name
        # 页码的队列
        self.page_queue = page_queue
        # 数据的队列
        self.data_queue = data_queue
        # 默认请求头
        self.header = {
            "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding":
            "gzip, deflate, br",
            "Accept-Language":
            "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6",
            "Connection":
            "keep-alive",
            "Host":
            "search.51job.com",
            "Upgrade-Insecure-Requests":
            "1",
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }

    def run(self):
        print("当前处理页码的任务为：%s" % self.thread_name)
        while not page_flag:
            try:
                page = self.page_queue.get(block=False)
                page_url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2," + str(
                    page) + ".html"
                #?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
                print("当前构造的url为：%s" % page_url)
                # 请求当前构造的url
                # 设置代理
                proxy = {
                    "http":
                    "http://HL097N676N1G511D:B9E2A683CECCC50B@http-dyn.abuyun.com:9020",
                    "https":
                    "https://HL097N676N1G511D:B9E2A683CECCC50B@http-dyn.abuyun.com:9020"
                }
                #加上代理
                result = requests.get(url=page_url,
                                      headers=self.header,
                                      proxies=proxy)
                result.encoding = "gbk"
                # 将我们请求回来的网页文本数据放到队列里面去
                self.data_queue.put(result.text)
            except:
                pass


# 处理网页文本数据处理类
class CrawlHtml(threading.Thread):
    # 从页码解析过来的文本数据，需要保存到data_queue里面去
    def __init__(self, thread_name, data_queue, lock):
        super(CrawlHtml, self).__init__()
        self.thread_name = thread_name
        self.data_queue = data_queue
        self.lock = lock

    def run(self):
        print("当前处理文本任务的线程为 %s" % self.thread_name)
        while not data_flag:
            try:
                # 取出文本数据
                text = self.data_queue.get(block=False)
                # 进行文本处理
                result = self.parse(text)
                with self.lock:
                    insert_data.insert_db(result)
            except:
                pass

    def parse(self, text):
        # HTML的实例化
        html_51job = etree.HTML(text)
        all_div = html_51job.xpath("//div[@id='resultList']//div[@class='el']")
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
            info_list.append(info)
        return info_list


# 定义两个全局的flag
page_flag = False
data_flag = False


def main():
    # 定义两个队列，用于存放页面队列和数据队列
    page_queue = Queue()
    data_queue = Queue()

    #定义一个线程锁
    lock = threading.Lock()

    # 将页码放入到页面队列里面去
    for page in range(1, 721):
        page_queue.put(page)

    # 打印当前队列的长度
    # print("当前页码的总量为 %s" % page_queue.qsize())  Mac端不能使用qsize()

    # 列表，包含了线程的名称
    crawl_page_list = ["页码处理线程1号", "页码处理线程2号", "页码处理线程3号"]
    page_thread_list = []
    for thread_name_page in crawl_page_list:
        thread_page = CrawlPage(thread_name_page, page_queue, data_queue)
        # 启动线程
        thread_page.start()
        page_thread_list.append(thread_page)

    # 设置3个线程，用于处理文本数据
    parse_list = ["文本线程1号", "文本线程2号", "文本线程3号"]
    parse_thread_list = []
    for thread_name_parse in parse_list:
        thread_parse = CrawlHtml(thread_name_parse, data_queue, lock)
        thread_parse.start()
        parse_thread_list.append(thread_parse)

    # 设置线程的退出机制
    global page_flag
    while not page_queue.empty():
        pass
    page_flag = True
    # 结束页码处理线程
    for thread_page_join in page_thread_list:
        thread_page_join.join()
        print(thread_page_join.thread_name, '处理结束')

    global data_flag
    while not data_queue.empty():
        pass
    data_flag = True

    for thread_parse_join in parse_thread_list:
        thread_page_join.join()
        print(thread_parse_join.thread_name, "文本处理结束")


if __name__ == "__main__":
    main()
