# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class TubatuScrapyPipeline(object):
    def __init__(self):
        myclient = pymongo.MongoClient("127.0.0.1:27017")
        mydb = myclient['db_tubatu']
        self.mycollection = mydb['collection_tubatu']

    def process_item(self, item, spider):
        data = dict(item)
        self.mycollection.insert_one(data)
        return item


# 自定义的图片下载类需要继承ImagesPipeline
class TubatuImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        """
        根据images_urls中指定的URL进行爬取
        :param item:
        :param info:
        :return:
        """

    def item_completed(self, results, item, info):
        """
        图片下载之后，返回一个处理结果，是一个二元祖格式的数据
        (success,images_info_or_failure)
        :param results:
        :param item:
        :param info:
        :return:
        """
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    def file_path(self, request, response=None, info=None):
        # 用于给下载的图片设置文件名称所用
        url = request.url
        file_name = url.split("/")[-1]
        # aaaa.jpg
        return file_name
