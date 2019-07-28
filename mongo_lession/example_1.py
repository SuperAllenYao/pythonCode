#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mongo_db import client

# client.school.teacher.insert_one({"name": "李璐"})
client.school.student.insert_many([{
    "name": "Scott"
}, {
    "name": "刘娜"
}, {
    "name": "陈浩"
}, {
    "name": "赵婷婷"
}])
