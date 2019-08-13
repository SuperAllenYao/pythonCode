#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TubatuScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 装修效果图标题
    content_name = scrapy.Field()
    # 装修ID
    content_id = scrapy.Field()
    # 请求url
    content_url = scrapy.Field()
    # 上传者昵称
    nick_name = scrapy.Field()
    # 图片url
    # pic_url = scrapy.Field()
    # 必须使用此变量
    image_urls = scrapy.Field()
    # 图片的名称
    pic_name = scrapy.Field()
