#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import etree
import json

# 要请求的URL
url = "https://search.51job.com/list/040000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

# 构造请求头数据
header = {
    "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding":
    "gzip, deflate, br",
    "Accept-Language":
    "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6",
    "Connection":
    "keep-alive",
    "Cookie":
    "guid=e3b41a72b0adf0189d33935c39d33978; 51job=cenglish%3D0%26%7C%26; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60040000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%601%A1%FB%A1%FA040000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1565065095%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch1%7E%601%A1%FB%A1%FA330000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1565065071%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21",
    "DNT":
    "1",
    "Host":
    "search.51job.com",
    "Upgrade-Insecure-Requests":
    "1",
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

result = requests.get(url=url, headers=header)
result.encoding = "gbk"
# print(result.text)
html_51job = etree.HTML(result.text)
all_div = html_51job.xpath("//div[@id='resultList']//div[@class='el']")
info_list = []
for item in all_div:
    info = {}
    # . 代表的是使用item下的Xpath语句
    # 获取数据的时候，要使用列表索引为0的数据
    info['jobname'] = item.xpath("./p/span/a/@title")[0]
    info['company_name'] = item.xpath(".//span[@class='t2']/a/@title")[0]
    info['company_address'] = item.xpath(".//span[@class='t3']/text()")[0]
    temp = item.xpath(".//span[@class='t4']/text()")
    if len(temp) == 0:
        info['money'] = "无"
    else:
        info['money'] = item.xpath(".//span[@class='t4']/text()")[0]
    info['date'] = item.xpath(".//span[@class='t5']/text()")[0]
    info_list.append(info)
print(info_list)
