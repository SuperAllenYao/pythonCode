#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#向 mongodb数据库保存文件
from mongo_db import client
from gridfs import GridFS

db = client.school
gfs = GridFS(db, collection="book")
files = open("/Users/superallen/Desktop/myCode/演示文件.txt", "rb")
args = {"type": "txt", "keyword": "file"}
gfs.put(files, filename="演示文件.txt", **args)
files.close()
