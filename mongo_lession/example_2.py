#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mongo_db import client

try:
    result = client.school.teacher.find({})
    for one in result:
        print(one["_id"], one["name"])
    print("---------------------------------")
    result = client.school.teacher.find_one({"name": "李璐"})
    print(result["_id"], result["name"])
except Exception as e:
    print(e)