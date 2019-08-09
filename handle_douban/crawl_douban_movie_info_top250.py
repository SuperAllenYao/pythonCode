#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
from handle_douban.handle_mongo import douban_mongo


class HandleDoubanMovieTop250(object):
    # 通过构造方法重写父类
    def __init__(self, header, page_url_list=[]):
        super(HandleDoubanMovieTop250, self).__init__()
        self.header = header
        self.page_url_list = page_url_list

    def handle_page_url(self):
        data_count = 0
        while data_count <= 250:
            url = "https://movie.douban.com/top250?start=" + str(
                data_count) + "&filter="
            data_count += 25
            self.page_url_list.append(url)
        return self.page_url_list

    def handle_request(self, url):
        proxy = {
            "http":
            "http://HL097N676N1G511D:B9E2A683CECCC50B@http-dyn.abuyun.com:9020",
            "https":
            "https://HL097N676N1G511D:B9E2A683CECCC50B@http-dyn.abuyun.com:9020"
        }
        result = requests.get(url=url, headers=self.header, proxies=proxy)
        result.encoding = "utf-8"
        print("文本数据为", result.text)
        return result.text

    def handle_page_detail(self, html_text, url):
        data = etree.HTML(html_text)
        all_div = data.xpath("//div[@class='info']")
        data_list = []
        movie_info = {}
        for item in all_div:
            movie_info['电影名称信息'] = item.xpath(
                ".//div[@class='hd']/a//span/text()")
            movie_info['电影演职人员信息'] = item.xpath(
                ".//div[@class='bd']/p[@class='']/text()")
            movie_info['电影评分数值'] = item.xpath(
                ".//div[@class='bd']/div[@class='star']//span[@property='v:average']/text()"
            )
            movie_info['评价数信息'] = item.xpath(
                ".//div[@class='bd']/div[@class='star']/span[last()]/text()")
            movie_info['电影简述信息'] = item.xpath(
                ".//div[@class='bd']/p[@class='quote']/span/text()")
            movie_info['来源URL信息'] = item.xpath(url)
        data_list.append(movie_info)
        print("这次爬到的数据是：", data_list)
        return data_list

    def run(self, list_data):
        executor = ThreadPoolExecutor(max_workers=4)
        task1 = executor.submit(self.task, list_data)
        print("任务1 已经开始了")
        task2 = executor.submit(self.task, list_data)
        print("任务2 已经开始了")
        task3 = executor.submit(self.task, list_data)
        print("任务3 已经开始了")
        task4 = executor.submit(self.task, list_data)
        print("任务4 已经开始了")
        if task1.done() and task2.done() and task3.done() and task4.done(
        ) == True:
            executor.shutdown()

    def task(self, url_list):
        for url in url_list:
            result = self.handle_request(url)
            print("文本数据为：", result)
            html_data = self.handle_page_detail(result, url)
            print("数据为：", html_data)
            douban_mongo.handle_save_data(html_data)
        print("数据为：", html_data)


def main():
    header = {
        "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding":
        "gzip, deflate, br",
        "Accept-Language":
        "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6",
        "Connection":
        "keep-alive",
        "Host":
        "movie.douban.com",
        "Upgrade-Insecure-Requests":
        "1",
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }
    douban = HandleDoubanMovieTop250(header)
    page_url_list = douban.handle_page_url()
    print("url已全部加入列表中", page_url_list)

    douban.run(page_url_list)


if __name__ == "__main__":
    main()