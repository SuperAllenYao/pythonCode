# -*- coding: utf-8 -*-
import scrapy
import re
import json
from tubatu_scrapy.tubatu_scrapy.items import TubatuScrapyItem


class TubatuSpider(scrapy.Spider):
    # 名称不能冲突，也不能重复
    name = 'tubatu'
    # 允许爬虫去抓去的域名
    allowed_domains = ['xiaoguotu.to8to.com']
    # 项目启动之后要第一个抓取的url
    start_urls = ['https://xiaoguotu.to8to.com/tuce/p_1.html']

    # 默认的解析方法
    def parse(self, response):
        print(response.request.headers)
        # 使用正则表达式来获取项目的id，使用/来转义.html
        content_id_search = re.compile(r"(\d+)\.html")
        # response 后面可以直接使用xpath方法
        # response 就是一个xpath对象
        pic_item_list = response.xpath("//div[@class='item']")
        for item in pic_item_list:
            info = {}
            info["content_name"] = item.xpath(
                ".//div/a/text()").extract_first()
            content_url = 'https:' + item.xpath(
                ".//div/a/@href").extract_first()
            info["content_id"] = content_id_search.search(content_url).group(1)
            info["content_ajax_url"] = "https://xiaoguotu.to8to.com/case/list?a2=0&a12=&a11=" + str(
                info["content_id"]) + "&a1=0&a17=1"
            # 使用 yield 来发送这个异步请求
            # 使用 scrapy.Request 发送请求
            # 回调函数，只写方法的名称，不需要调用方法
            yield scrapy.Request(url=info["content_ajax_url"], callback=self.handle_pic_parse, meta=info)
        # 页码的逻辑
        if response.xpath("//a[@id='nextpageid']"):
            now_page = int(response.xpath("//div[@class='pages']/strong/text()").extract_first())
            next_page_url = "https://xiaoguotu.to8to.com/tuce/p_%d.html" % (now_page + 1)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def handle_pic_parse(self, response):
        pic_dict_data = json.loads(response.text)["dataImg"]
        for pic_itme in pic_dict_data:
            for item in pic_itme['album']:
                tubatu_info = TubatuScrapyItem()
                # 昵称
                tubatu_info['nick_name'] = item["l"]["n"]
                # 图片地址
                # tubatu_info['pic_url'] = "https://pic1.to8to.com/case/" + item["l"]["s"]
                # 必须使用此字段，并传入一个列表格式
                tubatu_info['image_urls'] = ["https://pic1.to8to.com/case/" + item["l"]["s"]]
                # 图片的名称
                tubatu_info['pic_name'] = item["l"]["t"]
                tubatu_info['content_name'] = response.request.meta['content_name']
                tubatu_info['content_id'] = response.request.meta['content_id']
                tubatu_info["content_url"] = response.request.meta["content_ajax_url"]
                # yield 关键字会将数据传递到pipelines 里面去，需要在setting里面开启pipelines
                yield tubatu_info
