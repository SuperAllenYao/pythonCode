#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
from handle_douban.handle_mongo import douban_mongo


class HandleDoubanMovieTop250(object):
    # 通过构造方法重写父类
    def __init__(self, page_url_list=[]):
        super(HandleDoubanMovieTop250, self).__init__()
        # self.header = header
        self.page_url_list = page_url_list

    def handle_page_url(self):
        data_count = 0
        while data_count <= 225:
            url = "https://movie.douban.com/top250?start=" + str(
                data_count) + "&filter="
            data_count += 25
            self.page_url_list.append(url)
        print(self.page_url_list)

    def handle_request(self, url):
        # proxy = {
        #     "http":
        #     "http://HL097N676N1G511D:B9E2A683CECCC50B@http-dyn.abuyun.com:9020",
        #     "https":
        #     "https://HL097N676N1G511D:B9E2A683CECCC50B@http-dyn.abuyun.com:9020"
        # }
        result = requests.get(url=url)
        return result.text

    def handle_page_detail(self, html_text, url):
        data = etree.HTML(html_text)
        data_list = []
        all_div = data.xpath("//div[@class='info']")
        for item in all_div:
            movie_info = {}
            frist_data = item.xpath("./div[@class='hd']/a/span/text()")[0]
            second_data = item.xpath(
                "./div[@class='hd']/a//span[last()-1]/text()")[0]
            last_data = item.xpath(
                "./div[@class='hd']/a//span[last()]/text()")[0]
            movie_info['电影名称信息'] = frist_data + second_data + last_data
            str_name = str(
                item.xpath("./div[@class='bd']/p[@class='']/text()")[0])
            cc = str_name.lstrip()
            movie_info['电影演职人员信息'] = cc
            movie_info['电影评分数值'] = item.xpath(
                "./div[@class='bd']/div[@class='star']//span[@property='v:average']/text()"
            )[0]
            try:
                movie_info['评价数信息'] = item.xpath(
                    "./div[@class='bd']/div[@class='star']/span[last()]/text()"
                )[0]
            except:
                movie_info['评价数信息'] = "无"
            try:
                movie_info['电影简述信息'] = item.xpath(
                    "./div[@class='bd']/p[@class='quote']/span/text()")[0]
            except:
                movie_info['电影简述信息'] = "无"
            movie_info['来源URL信息'] = url
            data_list.append(movie_info)
        return data_list

    def run(self):
        executor = ThreadPoolExecutor(max_workers=1)
        for url in self.page_url_list:
            print("本次的url为：", url)
            executor.submit(self.task, url)
            print("URL {} 已经执行了".format(url))
        executor.shutdown()
        print("线程已关闭")

    def task(self, url):
        result = self.handle_request(url)
        html_data = self.handle_page_detail(result, url)
        print("正在插入的数据为：", url)
        douban_mongo.handle_save_data(html_data)


def main():
    # header = {
    #     "Accept":
    #     "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    #     "Accept-Encoding":
    #     "gzip, deflate, br",
    #     "Accept-Language":
    #     "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6",
    #     "Cache-Control":
    #     "max-age=0",
    #     "Connection":
    #     "keep-alive",
    #     "Cookie":
    #     "bid=0Iz7qicliqc; __utma=30149280.1616978889.1565343871.1565354901.1565411125.4; __utmc=30149280; __utmz=30149280.1565411125.4.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=223695111.1158322898.1565343871.1565354901.1565411125.4; __utmb=223695111.0.10.1565411125; __utmc=223695111; __utmz=223695111.1565411125.4.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt_t1=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1565411125%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utmb=30149280.6.8.1565411130337; _pk_id.100001.4cf6=672d650164751dcb.1565343871.4.1565411130.1565354901.; RT=s=1565411140523&r=https%3A%2F%2Fmovie.douban.com%2Ftop250",
    #     "DNT":
    #     "1",
    #     "Host":
    #     "movie.douban.com",
    #     "Referer":
    #     "https://www.google.com/",
    #     "Sec-Fetch-Mode":
    #     "navigate",
    #     "Sec-Fetch-Site":
    #     "none",
    #     "Sec-Fetch-User":
    #     "?1",
    #     "Upgrade-Insecure-Requests":
    #     "1",
    #     "User-Agent":
    #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    # }
    douban = HandleDoubanMovieTop250()
    douban.handle_page_url()
    douban.run()


if __name__ == "__main__":
    main()