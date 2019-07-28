#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mongo_db import client

result = client.school.student.find({}).skip(0).limit(10)
for one in result:
    print(one["_id"], one['name'])
print('----------------------------------------------')
result = client.school.student.distinct("name")
for one in result:
    print(one)
print('***************************************************')
result = client.school.student.find({}).sort([("name", -1)])
for one in result:
    print(one["_id"], one['name'])
