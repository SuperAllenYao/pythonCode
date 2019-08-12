# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.pipelines.images import ImagesPipline


class TubatuScrapyPipeline(object):
    def __init__(self):
        myclient = pymongo.MongoClient("127.0.0.1:27017")
        mydb = myclient['db_tubatu']
        self.mycollection = mydb['collection_tubatu']

    def process_item(self, item, spider):
        data = dict(item)
        self.mycollection.insert_one(data)
        return item


# 自定义的图片下载类需要继承ImagesPipline
class TubatuImagePipline(ImagesPipline):
    # def Image
    pass
