#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from db.mongo_db import client
from bson.objectid import ObjectId


class MongoNewsDao:
    # 添加新闻正文记录
    def insert(self, title, content):
        try:
            client.vega.news.insert_one({"title": title, "content": content})
        except Exception as e:
            print(e)

    # 查找新闻的主键值
    def search_news_id(self, title):
        try:
            news_id = client.vega.news.find_one({"title": title})
            return str(news_id["_id"])
        except Exception as e:
            print(e)

    # 修改新闻正文
    def update(self, id, title, content):
        try:
            client.vega.news.update_one(
                {"_id": object(id)},
                {"$set": {
                    "title": title,
                    "content": content
                }})
        except Exception as e:
            print(e)

    # 根据新闻的ID将新闻正文缓存到redis数据库中
    def search_content_id(self, id):
        try:
            news = client.vega.news.find_one({"_id": ObjectId(id)})
            return news["content"]
        except Exception as e:
            print(e)

    # 删除mongodb里面的新闻
    def delete_by_id(self, id):
        try:
            client.vega.news.delete_one({"_id": ObjectId(id)})
        except Exception as e:
            print(e)