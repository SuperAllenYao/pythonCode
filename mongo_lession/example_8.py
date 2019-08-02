#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mongo_db import client
from gridfs import GridFS
from bson.objectid import ObjectId

# 读取 mongodb 中存储的文件
db = client.school
gfs = GridFS(db, collection="book")
document = gfs.get(ObjectId("5d3dcfb971dd300a92291f68"))
files = open("/Users/superallen/Desktop/doc.txt", "wb")
files.write(document.read())
files.close()
