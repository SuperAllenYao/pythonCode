#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import etree

url = "https://movie.douban.com/top250?start=125&filter="
result = requests.get(url=url)
data = etree.HTML(result.text)
all_div = data.xpath("//div[@class='info']")
a = []
count = 0
for item in all_div:
    print("第【{}】次".format(count))
    count += 1
    movie_info = {}
    frist_data = item.xpath("./div[@class='hd']/a/span/text()")[0]
    second_data = item.xpath("./div[@class='hd']/a//span[last()-1]/text()")[0]
    last_data = item.xpath("./div[@class='hd']/a//span[last()]/text()")[0]
    movie_info['电影名称信息'] = frist_data + second_data + last_data
    movie_info['电影演职人员信息'] = str(
        item.xpath("./div[@class='bd']/p[@class='']/text()")[0]).lstrip()
    movie_info['电影评分数值'] = item.xpath(
        "./div[@class='bd']/div[@class='star']//span[@property='v:average']/text()"
    )[0]
    try:
        movie_info['评价数信息'] = item.xpath(
            "./div[@class='bd']/div[@class='star']/span[last()]/text()")[0]
    except:
        movie_info['评价数信息'] = "无"
    try:
        movie_info['电影简述信息'] = item.xpath(
            "./div[@class='bd']/p[@class='quote']/span/text()")[0]
    except:
        movie_info['电影简述信息'] = "无"
    movie_info['来源URL信息'] = url
    a.append(movie_info)
print(a)
