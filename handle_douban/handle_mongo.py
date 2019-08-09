#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient


class Handle_Mongo(object):
    def __init__(self):
        client = MongoClient(host="localhost", port=27017)
        mydb = client['douban']
        self.mycollection = mydb['data']

    def handle_save_data(self, data):
        self.mycollection.insert_many(data)


douban_mongo = Handle_Mongo()
