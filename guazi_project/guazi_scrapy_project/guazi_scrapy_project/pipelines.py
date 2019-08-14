# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from guazi_project.guazi_scrapy_project.guazi_scrapy_project.mongo_db import mongo


class GuaziScrapyProjectPipeline(object):
    def process_item(self, item, spider):
        mongo.save_data('guazi_data', item)
        return item
