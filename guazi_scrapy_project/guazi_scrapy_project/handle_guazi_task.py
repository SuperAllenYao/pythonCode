# -*- coding: utf-8 -*-
import requests
import execjs
import re
from guazi_scrapy_project.guazi_scrapy_project.mongo_db import mongo

# 请求城市的接口
url = "https://www.guazi.com/www/buy"
# 去掉cookie值，如长时间使用同一cookie值，对方会发现并对爬虫进行屏蔽
header = {
    "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,"
    "image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding":
    "gzip, deflate, br",
    "Accept-Language":
    "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6",
    "Connection":
    "keep-alive",
    "DNT":
    "1",
    "Host":
    "www.guazi.com",
    "Sec-Fetch-Mode":
    "navigate",
    "Sec-Fetch-Site":
    "none",
    "Upgrade-Insecure-Requests":
    "1",
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 ("
    "KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36 "
}

result = requests.get(url=url, headers=header)
# 设置返回的编码
result.encoding = "utf-8"
if "正在打开中,请稍后" in result.text:
    # 通过正则表达式获取了相关的字段和值
    value_search = re.compile(r"anti\('(.*?)','(.*?)'\);")
    string = value_search.search(result.text).group(1)
    key = value_search.search(result.text).group(2)
    # 读取破解的js文件
    with open("guazi.js", 'r') as f:
        f_read = f.read()
    # 使用execjs包来封装这段js
    js = execjs.compile(f_read)
    js_return = js.call('anti', string, key)
    cookie_value = 'antipas=' + js_return
    header['Cookie'] = cookie_value
    result_second = requests.get(url=url, headers=header)
    city_search = re.compile(r'href="/(.*?)/buy"\stitle="(.*?)">(.*?)</a>')
    brand_search = re.compile(r'href="\/www\/(.*?)\/c-1/#bread"\s+>(.*?)</a>')
    city_list = city_search.findall(result_second.text)
    brand_list = brand_search.findall(result_second.text)
    for city in city_list:
        if city[2] == '北京':
            for brand in brand_list:
                info = {}
                info['task_url'] = 'https://www.guazi.com/' + city[0] + '/' + \
                                   brand[0] + '/' + 'o1i7'
                info['city_name'] = city[1]
                info['brand_name'] = brand[1]
                info['item_type'] = 'list_item'
                mongo.save_task('guazi_task', info)
