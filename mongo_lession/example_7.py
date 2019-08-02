#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mongo_db import client
from gridfs import GridFS
from bson.objectid import ObjectId
import math
import datetime

db = client.school
gfs = GridFS(db, collection="book")
book = gfs.find_one({"filename": "演示文件.txt"})
print(book.filename)
print(book.type)
print(book.keyword)
print("%dM" % math.ceil(book.length / 1024 / 1024))

print('---------------------------------')
books = gfs.find({"type": "txt"})
for one in books:
    uploadDate = one.uploadDate + datetime.timedelta(hours=8)
    uploadDate = uploadDate.strftime("%Y-%m-%d %H:%M:%S")
    print(one._id, one.filename, uploadDate)
print('---------------------------------')
# exists函数查找文件是否存在
rs = gfs.exists(ObjectId("5d3dcfb971dd300a92291f68"))
print(rs)
rs = gfs.exists(**{"type": "txt"})
print(rs)
